from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

doc = SimpleDocTemplate(
    "report.pdf",
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Custom Title Style
title_style = ParagraphStyle(
    "CustomTitle",
    parent=styles["Title"],
    alignment=TA_CENTER,
    textColor=colors.HexColor("#1E3A8A"),
    fontSize=24,
    spaceAfter=20
)

title = Paragraph("Student Result Report 2026", title_style)

# Summary Text
summary = Paragraph(
    "<b>Student Performance Summary</b><br/>"
    "The student achieved excellent results across all courses.",
    styles["BodyText"]
)

table_data = [
    ["Course Name", "Mark", "Grade"],
    ["Data Structure", 87, "A+"],
    ["Algorithms", 90, "A+"],
    ["Machine Learning", 85, "A+"]
]

table = Table(
    table_data,
    colWidths=[220, 80, 80]
)

table.setStyle(TableStyle([
    # Header
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563EB")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 12),

    # Body
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 1), (-1, -1), 11),

    # Alignment
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

    # Alternate Row Colors
    ("BACKGROUND", (0, 1), (-1, 1), colors.whitesmoke),
    ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#E0F2FE")),
    ("BACKGROUND", (0, 3), (-1, 3), colors.whitesmoke),

    # Grid
    ("GRID", (0, 0), (-1, -1), 1, colors.grey),

    # Padding
    ("TOPPADDING", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
]))

elements = [
    title,
    summary,
    Spacer(1, 20),
    table
]

doc.build(elements)

print("Professional PDF report generated successfully!")