from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from pathlib import Path
import smtplib

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

def send_student_email(student):

    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")

    subject = "Student Registration Successful"

    print("EMAIL_USER =", sender)
    print("EMAIL_PASSWORD loaded =", bool(password))

    body = f"""
    Hello {student.name},
    
    Your registration has been completed.
    Student ID: {student.student_id}
    Name: {student.name}
    
    Thank you.
    
    """

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = student.email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)