from pydantic import BaseModel


class StudentCreate(BaseModel):
    student_id: int
    name: str
    email: str


class StudentResponse(BaseModel):
    student_id: int
    name: str
    email: str

    class Config:
        from_attributes = True