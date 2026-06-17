from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id"),
        nullable=False
    )

    subject = Column(String, nullable=False)
    marks = Column(Integer, nullable=False)