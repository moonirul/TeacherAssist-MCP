

from app.db.database import SessionLocal
from app.services.student_service import create_student, get_students
from app.schemas.student import StudentCreate  # ✅ add this import


def create_student_tool(student_id: int, 
                        name: str,
                        email: str,
                        dept: str,
                        batch: str):
    db = SessionLocal()
    try:
        student = StudentCreate(          # ✅ wrap in schema object
            student_id=student_id,
            name=name,
            email=email,
            department=dept,             # note: schema uses "department" not "dept"
            batch=batch
        )
        return create_student(db, student)
    finally:
        db.close()


def get_students_tool():
    db = SessionLocal()
    try:
        return get_students(db)
    finally:
        db.close()