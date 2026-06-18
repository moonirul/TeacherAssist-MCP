from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.exam import ExamCreate, ExamResponse
from app.services.exam import create_exam, get_exams

router = APIRouter()


# Create Exam
@router.post("/", response_model=ExamResponse)
def add_exam(
    exam: ExamCreate,
    db: Session = Depends(get_db)
):
    return create_exam(db, exam)


# Get all exams
@router.get("/", response_model=List[ExamResponse])
def list_exams(db: Session = Depends(get_db)):
    return get_exams(db)