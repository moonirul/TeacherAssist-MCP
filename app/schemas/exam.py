from pydantic import BaseModel


class ExamCreate(BaseModel):
    exam_name: str
    semester: str


class ExamResponse(BaseModel):
    exam_id: int
    exam_name: str
    semester: str

    class Config:
        from_attributes = True