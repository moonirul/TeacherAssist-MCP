# TeacherAssist-MCP

AI-powered Teacher Assistance MCP Server built with FastMCP, PostgreSQL, and SQLAlchemy.

This project demonstrates how to create a Model Context Protocol (MCP) server that allows AI assistants such as Claude Desktop to manage student records through MCP tools.

## Features

* Create students
* Retrieve all students
* PostgreSQL database integration
* SQLAlchemy ORM
* Claude Desktop MCP integration
* MCP Inspector support
* Beginner-friendly project structure

---

## Tech Stack

* Python 3.11+
* FastMCP
* PostgreSQL
* SQLAlchemy
* Psycopg2
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
│   ├── services/
│   │   └── student_service.py
│   │
│   ├── mcp/
│   │   ├── server.py
│   │   └── tools/
│   │       └── student_tools.py
│   │
│   └── main.py
│
├── .env
├── requirements.txt
├── README.md
└── pyproject.toml
```

---

## Prerequisites

Install:

* Python 3.11 or newer
* PostgreSQL
* Git

Verify installations:

```bash
python --version
psql --version
git --version
```

---

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/TeacherAssist-MCP.git

cd TeacherAssist-MCP
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

Using pip:

```bash
pip install -r requirements.txt
```

Or using uv:

```bash
uv sync
```

---

## PostgreSQL Setup

Create a database:

```sql
CREATE DATABASE teacherassist;
```

Create a PostgreSQL user if needed:

```sql
CREATE USER teacheruser WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE teacherassist TO teacheruser;
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://teacheruser:password@localhost:5432/teacherassist
```

Example:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/teacherassist
```

---

## Database Initialization

Start PostgreSQL.

Run the project once to create tables automatically if your project uses:

```python
Base.metadata.create_all(bind=engine)
```

Otherwise create tables manually.

---

## Run MCP Server

### Method 1

```bash
python -m app.mcp.server
```

### Method 2

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

Install Inspector:

```bash
npx @modelcontextprotocol/inspector
```

Run:

```bash
npx @modelcontextprotocol/inspector python -m app.mcp.server
```

or

```bash
npx @modelcontextprotocol/inspector uv run python -m app.mcp.server
```

Open the provided localhost URL.

Test tools:

* create_student
* get_students

---

## Claude Desktop Integration

Locate Claude Desktop MCP configuration file.

Add:

```json
{
  "mcpServers": {
    "Teacher-Assistance": {
      "command": "D:\\path\\to\\project\\.venv\\Scripts\\python.exe",
      "args": [
        "-m",
        "app.mcp.server"
      ],
      "cwd": "D:\\path\\to\\project"
    }
  }
}
```

Replace paths with your own installation paths.

Restart Claude Desktop.

---

## Example Tool Usage

Create Student:

```json
{
  "student_id": 101,
  "name": "Monirul Islam"
}
```

Response:

```json
{
  "student_id": 101,
  "name": "Monirul Islam"
}
```

Get Students:

```json
[
  {
    "student_id": 101,
    "name": "Monirul Islam"
  }
]
```

---

## Common Issues

### PostgreSQL Connection Error

Verify:

* PostgreSQL service is running
* Database exists
* Username/password are correct
* DATABASE_URL is correct

---

### ModuleNotFoundError: app

Run from project root:

```bash
cd TeacherAssist-MCP

python -m app.mcp.server
```

---

### Claude Desktop Cannot Connect

Verify:

* Virtual environment path is correct
* `cwd` points to project root
* MCP server starts manually
* Claude Desktop has been restarted

---

### Duplicate Key Error

```text
duplicate key value violates unique constraint
```

Cause:

Student ID already exists.

Solution:

Use a new unique `student_id`.

---

## Future Enhancements

* Update Student
* Delete Student
* Add Marks
* Grade Generation
* Attendance Management
* Student Reports
* AI-powered Academic Analytics
* FastAPI REST API
* Authentication and Authorization

---

## License

MIT License

Feel free to use, modify, and contribute.

---

## Author

Monirul Islam

TeacherAssist-MCP is a beginner-friendly MCP project demonstrating how AI assistants can interact with PostgreSQL databases through the Model Context Protocol (MCP).
