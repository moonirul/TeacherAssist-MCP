from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.subject import SubjectCreate
from app.services.subject import create_subject, get_subjects

router = APIRouter()

@router.post("/")
def add_subject(subject: SubjectCreate,
                db: Session = Depends(get_db)):
    return create_subject(db, subject)

@router.get("/")

def list_subjects(db:Session = Depends(get_db)):

    return get_subjects(db)