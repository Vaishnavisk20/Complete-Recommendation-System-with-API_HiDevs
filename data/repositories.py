from sqlalchemy.orm import Session
from data import models

class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id):
        return self.db.query(models.User).filter_by(id=user_id).first()

class ContentRepo:
    def __init__(self, db: Session):
        self.db = db

    def all(self):
        return self.db.query(models.Content).all()

class InteractionRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_user_history(self, user_id):
        return self.db.query(models.Interaction).filter_by(user_id=user_id).all()

    def add_feedback(self, user_id, content_id, rating):
        interaction = models.Interaction(
            user_id=user_id,
            content_id=content_id,
            rating=rating,
            type="feedback"
        )
        self.db.add(interaction)
        self.db.commit()