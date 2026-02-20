# Note Taking API (FastAPI)

A structured backend API built with FastAPI for managing notes.

This API supports full CRUD operations along with filtering, search, and pagination.

## 🚀 Tech Stack

- Python 3.12
- FastAPI
- Pydantic

## 📂 Project Structure

```
app/
│
├── main.py          # FastAPI app entrypoint
├── models.py        # Pydantic models
├── db.py            # In-memory storage
└── routers/
    └── notes.py     # Notes CRUD endpoints
```

## ⚙️ Installation & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/suleymangulymalikov/note_taking_api.git
cd note_taking_app
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

### Activate:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the development server

```bash
fastapi dev app/main.py
```

Server runs at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

## 📌 Features

### ✅ CRUD Operations

- Create a note
- Retrieve all notes
- Retrieve a single note by ID
- Update a note
- Delete a note

### ✅ Filtering

- Filter notes by tag

Example:

```
GET /notes?tag=work
```

### ✅ Search

- Case-insensitive
- Partial match
- Searches in title and content

Example:

```
GET /notes?search=python
```

### ✅ Pagination

- `skip`
- `limit`
- Input validation applied

Example:

```
GET /notes?skip=0&limit=10
```

## 📡 Example Combined Query

```
GET /notes?tag=work&search=python&skip=0&limit=5
```

Filtering is applied before pagination.
The original dataset remains unchanged during read operations.

## 🧠 Notes

- In-memory storage is used (no database).
- Project is structured for easy extension and scalability.

## 🎥 Preview

https://github.com/user-attachments/assets/a61ec43d-fbc1-4155-ae64-215a4a5c6ebf


