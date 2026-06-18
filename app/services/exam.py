from sqlalchemy.orm import Session

from app.models.exam import Exam
from app.schemas.exam import ExamCreate


def create_exam(db: Session, exam: ExamCreate):

    existing = (
        db.query(Exam)
        .filter(
            Exam.exam_name == exam.exam_name,
            Exam.semester == exam.semester
        )
        .first()
    )

    if existing:
        return existing

    new_exam = Exam(
        exam_name=exam.exam_name,
        semester=exam.semester,
    )

    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)

    return new_exam


def get_exams(db: Session):
    return db.query(Exam).all()