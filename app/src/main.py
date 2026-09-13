from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from sqlalchemy.orm import Session

from .database import get_db
from .models import TaskModel

app = FastAPI(
    title="Cloud-Native Task Management Platform",
    version="1.0.0"
)

class Task(BaseModel):
    title: str
    completed: bool = False

@app.get("/")
def root():
    return {"message": "Cloud-Native Task Management Platform is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

@app.post("/tasks")
def create_task(task: Task, db: Session = Depends(get_db)):
    new_task = TaskModel(
        title=task.title,
        completed=task.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {
        "id": new_task.id,
        "title": new_task.title,
        "completed": new_task.completed
    }

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).all()
    return [
        {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
        for task in tasks
    ]

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):
    existing_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    existing_task.title = task.title
    existing_task.completed = task.completed
    db.commit()
    db.refresh(existing_task)
    return {
        "id": existing_task.id,
        "title": existing_task.title,
        "completed": existing_task.completed
    }

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {
        "message": "Task deleted",
        "task": {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
    }
