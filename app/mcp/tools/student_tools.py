from app.db.database import SessionLocal
from app.services.student_service import create_student, get_students


def create_student_tool(student_id: int, 
                        name: str,
                        email: str):
    db = SessionLocal()
    try:
        return create_student(db, 
                              student_id, 
                              name,
                              email)
    finally:
        db.close()


def get_students_tool():
    db = SessionLocal()
    try:
        return get_students(db)
    finally:
        db.close()