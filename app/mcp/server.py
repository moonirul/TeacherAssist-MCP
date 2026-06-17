from fastmcp import FastMCP
from app.mcp.tools.student_tools import (
    create_student_tool,
    get_students_tool
)

from app.mcp.tools.mark_tools import (
    add_mark_tool,
    get_marks_tool
)

mcp = FastMCP("TeacherAssist-MCP")


@mcp.tool()
def create_student(student_id: int, name: str, email: str):
    """
    Create a new student in the database.

    Args:
        student_id: Unique student ID.
        name: Student full name.

    Returns:
        Student information after creation.
    """
    return create_student_tool(student_id, name, email)


@mcp.tool()
def get_students():
    
    """
    Get all students from the database.

    Returns:
        List of all students.
    """
    return get_students_tool()


@mcp.tool()
def add_mark(
    student_id: int,
    subject: str,
    marks: int
):
    return add_mark_tool(
        student_id,
        subject,
        marks
    )


@mcp.tool()
def get_marks():
    return get_marks_tool()


if __name__ == "__main__":
    mcp.run()