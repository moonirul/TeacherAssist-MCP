from sqlalchemy.orm import Session

from app.models.mark import Mark
from app.models.student import Student


def add_mark(db: Session, student_id: int, subject: str, marks: int):

    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if not student:
        return {"error": "Student not found"}

    mark = Mark(
        student_id=student_id,
        subject=subject,
        marks=marks
    )

    db.add(mark)
    db.commit()
    db.refresh(mark)

    return {
        "id": mark.id,
        "student_id": mark.student_id,
        "subject": mark.subject,
        "marks": mark.marks
    }


def get_marks(db: Session):

    marks = db.query(Mark).all()

    return [
        {
            "student_id": m.student_id,
            "subject": m.subject,
            "marks": m.marks
        }
        for m in marks
    ]