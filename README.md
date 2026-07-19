# 🎓 TeacherAssist-MCP

AI-powered **Teacher Assistant MCP Server** built with **FastMCP, FastAPI, PostgreSQL, SQLAlchemy, ReportLab, and automated email notifications**.

TeacherAssist-MCP allows AI assistants such as **Claude Desktop** to manage student records through **Model Context Protocol (MCP) tools** while also exposing a robust **FastAPI REST API** for traditional integrations.

---

## 🎥 Demo Video

▶️ **Watch the complete project demo:** [TeacherAssist-MCP Demo Video](https://drive.google.com/file/d/1YjF5oDgX5hwEcqKxGphxi_i3ndqEU-g9/view?usp=sharing)

---

## 🚀 Project Overview

TeacherAssist-MCP is a modern **AI-integrated teacher management system** designed to simplify academic administration. It combines the power of **FastAPI** with **FastMCP** to provide both traditional REST APIs and AI-powered MCP tools.

With this system, educators and AI assistants can:

* 👨‍🎓 Manage student records
* 📚 Handle subjects and exams
* 📝 Store and retrieve marks
* 📊 Calculate GPA automatically
* 📑 Generate academic reports
* 📧 Send automated email notifications
* 🤖 Integrate seamlessly with Claude Desktop via MCP

This project demonstrates how **AI assistants can interact with PostgreSQL databases through MCP tools** while maintaining a clean, scalable, and production-ready backend architecture.

---

## ✨ Features

### 👨‍🎓 Student Management

* Create new student records
* Retrieve all students
* Store student information securely in PostgreSQL
* Send automatic registration confirmation emails

### 📚 Academic Management

* Create and manage subjects
* Create and manage exams
* Store student marks for each exam

### 📊 Reporting & GPA

* Calculate GPA automatically
* Generate student performance reports
* Export reports as PDF using ReportLab

### 🤖 MCP Integration

* Claude Desktop MCP integration
* MCP Inspector support
* AI-powered database interaction through FastMCP tools

---

## 🛠️ Tech Stack

| Technology     | Purpose                     |
| -------------- | --------------------------- |
| Python 3.11+   | Core programming language   |
| FastAPI        | REST API framework          |
| FastMCP        | MCP server framework        |
| PostgreSQL     | Relational database         |
| SQLAlchemy     | ORM for database operations |
| Psycopg2       | PostgreSQL adapter          |
| ReportLab      | PDF report generation       |
| Gmail SMTP     | Email notifications         |
| UV             | Package management          |
| Claude Desktop | AI assistant integration    |

---

## 📂 Project Structure

```text
TeacherAssist-MCP/
│
├── app/
│   ├── db/                    # Database configuration
│   ├── models/                # SQLAlchemy models
│   │   ├── student.py
│   │   ├── subject.py
│   │   ├── exam.py
│   │   └── mark.py
│   ├── schemas/               # Pydantic schemas
│   ├── routes/                # FastAPI routes
│   ├── services/              # Business logic
│   ├── mcp/                   # MCP server and tools
│   │   ├── server.py
│   │   └── tools/
│   │       ├── student_tools.py
│   │       └── mark_tools.py
│   └── main.py                # FastAPI entry point
│
├── report-lab/                # Report generation utilities
├── reports/                   # Generated reports
├── .env                       # Environment variables
├── pyproject.toml             # Project dependencies
├── uv.lock                    # Dependency lock file
├── README.md                  # Project documentation
└── LICENSE
```

---

## ⚙️ Prerequisites

Before running this project, make sure you have installed:

* **Python 3.11+**
* **PostgreSQL**
* **Git**
* **UV Package Manager**

### Verify Installation

```bash
python --version
git --version
psql --version
uv --version
```

---

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/TeacherAssist-MCP.git

cd TeacherAssist-MCP
```

### 2️⃣ Install Dependencies

```bash
uv sync
```

### 3️⃣ Activate Virtual Environment

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

---

## 🗄️ PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE teacherassist;
```

---

## 🔐 Environment Variables

Create a **.env** file in the project root and add the following:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/teacherassist

EMAIL_USER=[your_email@gmail.com](mailto:your_email@gmail.com)
EMAIL_PASSWORD=your_gmail_app_password
```

### Gmail Configuration

To enable email notifications:

* Enable **2-Step Verification** in your Google Account.
* Generate a **Google App Password**.
* Use the generated password as **EMAIL_PASSWORD**.
* **Do NOT** use your normal Gmail password.

---

## ▶️ Running the Application

### Run FastAPI Server

```bash
uv run uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

### Run MCP Server

```bash
uv run python -m app.mcp.server
```

Expected output:

```text
Starting MCP server 'TeacherAssist MCP'
transport 'stdio'
```

---

## 🧪 Testing with MCP Inspector

Run the following command:

```bash
npx @modelcontextprotocol/inspector uv run python -m app.mcp.server
```

Open the generated URL in your browser to inspect available MCP tools.

### Available MCP Tools

* **create_student**
* **get_students**
* **create_mark**
* **get_student_marks**

---

## 🤖 Claude Desktop Integration

Add the following configuration to your **Claude Desktop MCP config file**:

```json
{
"mcpServers": {
"Teacher-Assistance": {
"command": "C:\Monirul\TeacherAssist-MCP\.venv\Scripts\python.exe",
"args": [
"-m",
"app.mcp.server"
],
"cwd": "C:\Monirul\TeacherAssist-MCP"
}
}
}
```

Replace the paths with your own project location, then restart **Claude Desktop**.

---

## 📡 API Endpoints

### Student Endpoints

| Method | Endpoint  | Description           |
| ------ | --------- | --------------------- |
| POST   | /students | Create a new student  |
| GET    | /students | Retrieve all students |

### Subject Endpoints

| Method | Endpoint  | Description           |
| ------ | --------- | --------------------- |
| POST   | /subjects | Create a subject      |
| GET    | /subjects | Retrieve all subjects |

### Exam Endpoints

| Method | Endpoint | Description        |
| ------ | -------- | ------------------ |
| POST   | /exams   | Create an exam     |
| GET    | /exams   | Retrieve all exams |

### Mark Endpoints

| Method | Endpoint                    | Description             |
| ------ | --------------------------- | ----------------------- |
| POST   | /marks                      | Create a mark entry     |
| GET    | /marks/student/{student_id} | Get marks by student ID |

---

## 📝 API Examples

### Create a Student

```http
POST /students
```

Request Body:

```json
{
"student_id": 101,
"name": "Monirul Islam",
"email": "[student@example.com](mailto:student@example.com)"
}
```

Response:

```json
{
"student_id": 101,
"name": "Monirul Islam",
"email": "[student@example.com](mailto:student@example.com)"
}
```

A confirmation email will automatically be sent to the student.

### Get Students

```http
GET /students
```

Response:

```json
[
{
"student_id": 101,
"name": "Monirul Islam",
"email": "[student@example.com](mailto:student@example.com)"
}
]
```

---

## 💬 Example Claude Desktop Prompts

> Create a student with ID 1001, name Monirul Islam, email [monirul@gmail.com](mailto:monirul@gmail.com)

> Show all students

> Create marks for student ID 1001 in Mathematics exam

> Calculate GPA for student ID 1001

Claude Desktop will automatically invoke the appropriate MCP tools.

---

## 🐛 Common Issues & Solutions

### ModuleNotFoundError: app

Run the MCP server from the project root:

```bash
uv run python -m app.mcp.server
```

### PostgreSQL Connection Error

* Ensure PostgreSQL service is running.
* Verify the database exists.
* Check database credentials in **.env**.
* Confirm **DATABASE_URL** is correct.

### Claude Desktop Cannot Connect

* Verify the correct Python executable path.
* Verify the correct **cwd** path.
* Ensure the MCP server runs manually without errors.
* Restart Claude Desktop after configuration changes.

### Gmail Authentication Failed

Use a **Google App Password** instead of your normal Gmail password.

---

## 🚀 Future Enhancements

* ✏️ Update Student
* 🗑️ Delete Student
* 📅 Attendance Management
* 📈 Advanced GPA Analytics
* 📑 PDF Report Export
* 🔐 Authentication & Authorization
* 👥 Multi-user Support
* 🤖 AI-powered Student Performance Insights

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request.

```bash
git checkout -b feature/your-feature-name
```

---

## 📄 License

This project is licensed under the **MIT License**. See the **LICENSE** file for more details.

---

## 👨‍💻 Author

**Monirul Islam**

* 🔗 GitHub: https://github.com/moonirul
* 💼 LinkedIn: https://linkedin.com/in/moonirul


---

## ⭐ Support

If you find this project useful, please consider giving it a **⭐ star on GitHub**. It helps the project reach more developers and supports future improvements.

---

**TeacherAssist-MCP** demonstrates how modern **AI assistants can interact with PostgreSQL databases through FastMCP and the Model Context Protocol (MCP)**, while integrating **FastAPI APIs, automated email notifications, GPA calculation, and report generation** in a scalable and production-ready architecture.
