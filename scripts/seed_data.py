from data.database import SessionLocal, engine
from data.models import Base, User, Content

def seed():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    for i in range(1, 11):
        db.add(User(id=i, name=f"User {i}", interests="AI"))

    for i in range(1, 21):
        db.add(Content(
            id=i,
            title=f"Course {i}",
            category="AI",
            difficulty="easy",
            popularity=20 - i
        ))

    db.commit()
    print("✅ Data Seeded!")

if __name__ == "__main__":
    seed()