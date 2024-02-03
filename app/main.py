# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import users
from app.api.routes import moviescreator
from app.api.models import models
from app.api.database import database
from app.api.auth import authentication
from app.core.config import settings


app = FastAPI(
    title="Direkto API",
    description="This is the API for the direkto project",
    version="0.0.1",
)

# Define CORS origins based on settings
origins = [
    # Replace with your actual allowed origins
    origin.strip()
    for origin in settings.origins.split(",")
]

# Add CORS middleware to allow specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "This is Direkto API v0.0.1"}


models.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(moviescreator.router, prefix="/moviecreators", tags=["creators"])
app.include_router(authentication.router, prefix="/auth", tags=["authentication"])
