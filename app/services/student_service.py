from sqlalchemy.orm import Session
from app.models.student import Student


def create_student(db: Session, student_id, name):
    existing = db.query(Student).filter(Student.student_id == student_id).first()

    if existing:
        return existing  # prevent crash

    student = Student(student_id=student_id, name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {
    "student_id": student.student_id,
    "name": student.name
}


def get_students(db: Session):
    students = db.query(Student).all()

    return [
        {
            "student_id": s.student_id,
            "name": s.name
        }
        for s in students
    ]