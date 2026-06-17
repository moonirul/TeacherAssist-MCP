# TeacherAssist-MCP

AI-powered Teacher Assistant MCP Server built with FastMCP, FastAPI, PostgreSQL, SQLAlchemy, and Email Notifications.

This project demonstrates how to build a Model Context Protocol (MCP) server that allows AI assistants such as Claude Desktop to manage student records through MCP tools while automatically sending registration emails to students.

---

## Features

* Create students
* Retrieve all students
* Email notification on student registration
* PostgreSQL database integration
* SQLAlchemy ORM
* FastAPI REST API
* Claude Desktop MCP integration
* MCP Inspector support
* Beginner-friendly project structure

---

## Tech Stack

* Python 3.11+
* FastMCP
* FastAPI
* PostgreSQL
* SQLAlchemy
* Psycopg2
* SMTP (Gmail)
* UV Package Manager
* Claude Desktop
* MCP Inspector

---

## Project Structure

```text
TeacherAssist-MCP/
│
├── app/
│   ├── db/
│   │   └── database.py
│   │
│   ├── models/
│   │   └── student.py
│   │
│   ├── schemas/
│   │   └── student.py
│   │
│   ├── services/
│   │   ├── student_service.py
│   │   └── email_service.py
│   │
│   ├── mcp/
│   │   ├── server.py
│   │   └── tools/
│   │       └── student_tools.py
│   │
│   └── main.py
│
├── .env
├── pyproject.toml
├── uv.lock
├── README.md
└── .venv/
```

---

## Prerequisites

Install:

* Python 3.11+
* PostgreSQL
* Git
* UV

Verify:

```bash
python --version
git --version
psql --version
uv --version
```

---

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/TeacherAssist-MCP.git

cd TeacherAssist-MCP
```

---

## Install Dependencies

Using UV:

```bash
uv sync
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## PostgreSQL Setup

Create database:

```sql
CREATE DATABASE teacherassist;
```

Example connection:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/teacherassist
```

---

## Email Configuration

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/teacherassist

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

### Gmail Setup

1. Enable 2-Step Verification
2. Open Google Account Security
3. Generate App Password
4. Use the generated password as `EMAIL_PASSWORD`

Do NOT use your Gmail login password.

---

## Run FastAPI Server

```bash
uv run uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI will be available for testing APIs.

---

## Run MCP Server

```bash
uv run python -m app.mcp.server
```

Expected output:

```text
Starting MCP server 'TeacherAssist MCP'
transport 'stdio'
```

---

## Test Using MCP Inspector

Run:

```bash
npx @modelcontextprotocol/inspector uv run python -m app.mcp.server
```

Open the generated URL.

Available tools:

* create_student
* get_students

---

## Claude Desktop Configuration

Open Claude Desktop MCP configuration file and add:

```json
{
  "mcpServers": {
    "Teacher-Assistance": {
      "command": "D:\\Projects\\TeacherAssist-MCP\\.venv\\Scripts\\python.exe",
      "args": [
        "-m",
        "app.mcp.server"
      ],
      "cwd": "D:\\Projects\\TeacherAssist-MCP"
    }
  }
}
```

Replace the paths with your own project location.

Restart Claude Desktop.

---

## API Examples

### Create Student

POST `/students`

```json
{
  "student_id": 101,
  "name": "Monirul Islam",
  "email": "student@example.com"
}
```

Response:

```json
{
  "student_id": 101,
  "name": "Monirul Islam",
  "email": "student@example.com"
}
```

A confirmation email will automatically be sent.

---

### Get Students

GET `/students`

Response:

```json
[
  {
    "student_id": 101,
    "name": "Monirul Islam",
    "email": "student@example.com"
  }
]
```

---

## Example Claude Desktop Prompts

```text
Create a student with ID 1001, name Monirul Islam, email monirul@gmail.com
```

```text
Show all students
```

Claude will invoke MCP tools automatically.

---

## Common Issues

### ModuleNotFoundError: app

Run from project root:

```bash
uv run python -m app.mcp.server
```

---

### PostgreSQL Connection Error

Verify:

* PostgreSQL service is running
* Database exists
* Credentials are correct
* DATABASE_URL is correct

---

### Claude Desktop Cannot Connect

Verify:

* Correct Python executable path
* Correct cwd path
* MCP server runs manually
* Claude Desktop restarted after config change

---

### Gmail Authentication Failed

Use a Google App Password.

Do not use your normal Gmail password.

---

### Duplicate Student ID

Student IDs must be unique.

Use a new ID when creating students.

---

## Future Enhancements

* Update Student
* Delete Student
* Attendance Management
* Grade Calculation
* GPA Calculation
* Student Reports
* AI-powered Analytics
* Authentication & Authorization
* Multi-user Support

---

## License

MIT License

---

## Author

Monirul Islam

TeacherAssist-MCP demonstrates how AI assistants can interact with PostgreSQL databases through FastMCP and the Model Context Protocol (MCP), while integrating FastAPI APIs and automated email notifications.
