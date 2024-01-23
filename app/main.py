# main.py
from fastapi import FastAPI
from app.api.routes import users
from app.api.models import models
from app.api.database import database


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router, prefix="/users", tags=["users"])
