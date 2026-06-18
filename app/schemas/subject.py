from pydantic import BaseModel


class SubjectCreate(BaseModel):
    subject_code: str
    subject_name: str
    credit: float


class SubjectResponse(BaseModel):
    subject_id: int
    subject_code: str
    subject_name: str
    credit: float

    class Config:
        from_attributes = True