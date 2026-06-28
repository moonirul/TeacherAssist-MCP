from app.db.database import SessionLocal
from app.services.mark import (
    create_mark,
    get_marks
)
from app.schemas.mark import MarkCreate


def add_mark_tool(student_id:int,
                  subject_id: int, 
                  exam_id: int,
                  marks_obtained: float
                  ):

    db = SessionLocal()

    try: 
        mark = MarkCreate(
            student_id=student_id,
            subject_id=subject_id,
            exam_id=exam_id,
            marks_obtained=marks_obtained
        )
        return create_mark(db, mark)
    finally:
        db.close()


def get_marks_tool():
    db = SessionLocal()
    try:
        return get_marks(db)
    finally:
        db.close()