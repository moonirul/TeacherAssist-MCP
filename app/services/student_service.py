from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate
from app.services.email_service import send_student_email


def create_student(db: Session, student:StudentCreate):
    existing = (
        db.query(Student)
                .filter(Student.student_id == student.student_id)
                .first()
                )

    if existing:
        return existing  # prevent crash

    new_student = Student(
        student_id=student.student_id,
        name= student.name,
        email=student.email,
        department = student.department,
        batch = student.batch
        )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    # send_student_email(new_student)

    return {
    "student_id": student.student_id,
    "name": student.name,
    "email": student.email,
    "department": student.department,
    "batch" : student.batch
}


def get_students(db: Session):
    students = db.query(Student).all()

    return [
        {
            "student_id": s.student_id,
            "name": s.name,
            "email": s.email,
            "department": s.department,
            "batch" : s.batch
        }
        for s in students
    ]
    
    
    
    
    





