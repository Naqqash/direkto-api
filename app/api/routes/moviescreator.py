from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import List, Annotated
from app.api.dependencies.tmdb import search_creator
from app.api.auth.authentication import get_current_user
from app.api.schemas.schemas import Creator, User


router = APIRouter()


@router.get("/search/{creator_name}", response_model=List[Creator])
def search_movie_creator(
    creator_name: str,
    current_user: Annotated[User, Depends(get_current_user)],
):
    # current_user now contains the authenticated user
    creators = search_creator(creator_name)
    if creators is None:
        raise HTTPException(
            status_code=404, detail="Creator not found or TMDB API error"
        )
    return creators
