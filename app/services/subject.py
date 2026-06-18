from sqlalchemy.orm import Session
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate

def create_subject(db: Session,
                   subject: SubjectCreate):
    existing = (
        db.query(Subject)
        .filter(Subject.subject_code==
        subject.subject_code).first()
    )

    if existing:
        return existing
    
    new_subject = Subject(
        subject_code = subject.subject_code,
        subject_name = subject.subject_name,
        credit = subject.credit
    )

    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)

    return new_subject

def get_subjects(db: Session):
    subjects = db.query(Subject).all()
    return subjects

