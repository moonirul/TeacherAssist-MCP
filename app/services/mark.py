from sqlalchemy.orm import Session

from app.models.mark import Mark
from app.schemas.mark import MarkCreate


def calculate_grade(marks: float) -> str:
    if marks >= 80:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 70:
        return "A-"
    elif marks >= 65:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 55:
        return "B-"
    elif marks >= 50:
        return "C+"
    elif marks >= 45:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def create_mark(db: Session, mark: MarkCreate):
    new_mark = Mark(
        student_id=mark.student_id,
        subject_id=mark.subject_id,
        exam_id=mark.exam_id,
        marks_obtained=mark.marks_obtained,
        grade=calculate_grade(mark.marks_obtained)
    )
    db.add(new_mark)
    db.commit()
    db.refresh(new_mark)
    
    return new_mark

    
def get_marks(db: Session):
    return db.query(Mark).all()
   


# GET MARKS BY STUDENT (VERY IMPORTANT FOR RESULT SYSTEM)
def get_marks_by_student(db: Session, student_id: int):
    return db.query(Mark).filter(Mark.student_id == student_id).all()