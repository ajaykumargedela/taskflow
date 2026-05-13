from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database.db import engine, Base, SessionLocal
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>TaskFlow</title></head>
        <body>
            <h1>TaskFlow App</h1>
            <form action="/submit" method="post">
                <input type="text" name="title" placeholder="Enter title" required><br><br>
                <input type="text" name="description" placeholder="Enter description" required><br><br>
                <button type="submit">Save Task</button>
            </form>
        </body>
    </html>
    """


@app.post("/submit")
def submit_task(title: str = Form(...), description: str = Form(...)):
    db = SessionLocal()

    new_task = Task(title=title, description=description)
    db.add(new_task)
    db.commit()

    return {"message": "Task saved to backend database"}


@app.post("/tasks")
def create_task(task: TaskCreate):
    db = SessionLocal()

    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title
        }
    }


@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    return tasks


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"message": "Task not found"}

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"message": "Task not found"}

    task.title = updated_task.title
    task.description = updated_task.description

    db.commit()

    return {
        "message": "Task updated successfully",
        "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description
        }
    }