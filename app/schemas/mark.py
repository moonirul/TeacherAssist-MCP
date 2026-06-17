from pydantic import BaseModel


class MarkCreate(BaseModel):
    student_id: int
    subject: str
    marks: int