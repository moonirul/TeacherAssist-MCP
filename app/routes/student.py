from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.student import StudentCreate
from app.services.student_service import create_student, get_students

router = APIRouter()


@router.post("/")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)


@router.get("/")
def list_students(db: Session = Depends(get_db)):
    return get_students(db)