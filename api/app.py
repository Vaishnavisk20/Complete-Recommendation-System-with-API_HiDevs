from fastapi import FastAPI, HTTPException, Header
import time

from data.database import SessionLocal, engine
from data import models
from data.repositories import UserRepo, ContentRepo, InteractionRepo
from engine.orchestrator import RecommendationOrchestrator

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

request_count = 0
API_KEY = "12345"

@app.middleware("http")
async def log_requests(request, call_next):
    global request_count
    request_count += 1

    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    print(f"Request {request_count} took {duration:.4f}s")
    return response

def verify_api_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.get("/")
def root():
    return {"message": "Recommendation API is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int, x_api_key: str = Header(...)):
    verify_api_key(x_api_key)

    db = SessionLocal()

    user_repo = UserRepo(db)
    user = user_repo.get(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    engine_obj = RecommendationOrchestrator(
        ContentRepo(db),
        InteractionRepo(db),
        user_repo
    )

    return engine_obj.get_recommendations(user_id)

@app.post("/feedback")
def feedback(user_id: int, content_id: int, rating: float):
    db = SessionLocal()
    InteractionRepo(db).add_feedback(user_id, content_id, rating)
    return {"message": "Feedback recorded"}

@app.get("/metrics")
def metrics():
    return {
        "total_requests": request_count
    }