from sqlalchemy import Column, Integer, String

from app.db.database import Base

class Exam(Base):
    __tablename__= "exams"
    
    exam_id = Column(Integer, primary_key=True, autoincrement=True)
    exam_name = Column(String, nullable=False)
    semester = Column(String, nullable=False)