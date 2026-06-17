from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.database import engine, Base, get_db
from app.models.student import Student
from app import models

from app.schemas.mark import MarkCreate
from app.services.mark_service import add_mark, get_marks


from app.schemas.student import StudentCreate
from app.services.student_service import create_student, get_students

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Teacher Assistant MCP Server",
    description="MCP backend for grading, GPA calculation, and report generation",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Teacher Assistant MCP Server is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


# ======================
# CREATE STUDENT
# ======================
@app.post("/students")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student.student_id, student.name, student.email)


# ======================
# GET STUDENTS
# ======================
@app.get("/students")
def list_students(db: Session = Depends(get_db)):
    return get_students(db)


@app.post("/marks")
def create_mark(mark: MarkCreate,
                db: Session = Depends(get_db)):

    return add_mark(
        db,
        mark.student_id,
        mark.subject,
        mark.marks
    )


@app.get("/marks")
def list_marks(db: Session = Depends(get_db)):
    return get_marks(db)