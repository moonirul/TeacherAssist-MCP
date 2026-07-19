from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.subject import Subject
from app.models.exam import Exam
from app.models.student import Student

from app.db.database import Base


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, autoincrement=True)

    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.exam_id"), nullable=False)

    marks_obtained = Column(Float, nullable=False)
    grade = Column(String, nullable=True)

    # relations
    student = relationship("Student", lazy="joined")
    subject = relationship("Subject", lazy="joined")
    exam = relationship("Exam", lazy="joined")