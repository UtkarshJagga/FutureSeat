from sqlalchemy.orm import Session
from app.models.college import College
from app.schemas.college import CollegeCreate


def list_colleges(db: Session):
    return db.query(College).all()


def create_college(db: Session, payload: CollegeCreate):
    obj = College(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj