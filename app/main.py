from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.database import engine, Base, get_db
from app.models.student import Student
from app import models


from app.schemas.student import StudentCreate

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


# CREATE STUDENT
@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        student_id=student.student_id,
        name=student.name
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student