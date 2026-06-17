from app.db.database import SessionLocal
from app.services.mark_service import (
    add_mark,
    get_marks
)


def add_mark_tool(student_id, subject, marks):

    db = SessionLocal()

    try:
        return add_mark(
            db,
            student_id,
            subject,
            marks
        )
    finally:
        db.close()


def get_marks_tool():

    db = SessionLocal()

    try:
        return get_marks(db)
    finally:
        db.close()