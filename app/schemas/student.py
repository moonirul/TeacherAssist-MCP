from pydantic import BaseModel
from datetime import datetime

class StudentCreate(BaseModel):
    student_id: int
    name: str
    email: str
    department: str
    batch: str
    


class StudentResponse(BaseModel):
    student_id: int
    name: str
    email: str
    department: str
    batch: str
    created_at: datetime
    

    class Config:
        from_attributes = True