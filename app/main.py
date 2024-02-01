# main.py
from fastapi import FastAPI
from app.api.routes import users
from app.api.routes import moviescreator
from app.api.models import models
from app.api.database import database
from app.api.auth import authentication


app = FastAPI(
    title="Direkto API",
    description="This is the API for the direkto project",
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "This is Direkto API v0.0.1"}


models.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(moviescreator.router, prefix="/moviecreators", tags=["creators"])
app.include_router(authentication.router, prefix="/auth", tags=["authentication"])
