from sqlalchemy import Column, Integer, String, Float

from app.db.database import Base
class Student(Base):
    __tablename__ = "students"
    
    student_id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = Column(String, nullable=False)
    
