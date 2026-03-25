from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.college import CollegeOut
from app.services.college_service import list_colleges

router = APIRouter()


@router.get("/colleges", response_model=list[CollegeOut])
def get_colleges(db: Session = Depends(get_db)):
    return list_colleges(db)