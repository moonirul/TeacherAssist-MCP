from sqlalchemy.orm import Session
from app.models.student import Student
from app.services.email_service import send_student_email


def create_student(db: Session, student_id, name, email):
    existing = db.query(Student).filter(Student.student_id == student_id).first()

    if existing:
        return existing  # prevent crash

    student = Student(student_id=student_id, name=name, email=email)
    db.add(student)
    db.commit()
    db.refresh(student)

    send_student_email(student)

    return {
    "student_id": student.student_id,
    "name": student.name,
    "email": student.email
}


def get_students(db: Session):
    students = db.query(Student).all()

    return [
        {
            "student_id": s.student_id,
            "name": s.name,
            "email": s.email
        }
        for s in students
    ]




