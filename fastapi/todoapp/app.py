from pathlib import Path
from pyexpat import model
from re import I
from typing_extensions import Required
from fastapi import FastAPI, Depends, Request, Form,status

from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from .database import SessionLocal, engine

from . import models

models.Base.metadata.create_all(bind=engine)

BASE_PATH = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def home(req: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()

    return templates.TemplateResponse("base.html", {"request":req, "todo_list":todos})

url = app.url_path_for("home")

@app.post("/add")
def add(req: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.Todo(title=title)
    db.add(new_todo)
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{todo_id}")
def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{todo_id}")
def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)