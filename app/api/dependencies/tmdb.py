import requests
from typing import List, Optional
from pydantic import BaseModel
from app.api.schemas.schemas import Creator, Movie


def search_creator(creator_name: str) -> Optional[List[Creator]]:
    url = f"https://api.themoviedb.org/3/search/person?query={creator_name}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZTBkZWMyMzU5YThlMDkxMmU5YWU4YzhmYTEzMjE3OSIsInN1YiI6IjY1YjUyZWMwNGYzM2FkMDE2MTBiNjQwZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-fBxxGdtCA6aljUMrAu6tSfw7MxeSpQLaTe5MMcSP8M",
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    creators = []
    for result in data.get("results", []):
        if result.get("known_for_department") == "Directing":
            movies = [
                Movie(
                    title=movie.get("title", ""),
                    overview=movie.get("overview", ""),
                    media_type=movie.get(
                        "media_type", "movie"
                    ),  # defaulting to 'movie'
                    popularity=movie.get("popularity", 0.0),
                )
                for movie in result.get("known_for", [])
            ]
            creators.append(
                Creator(
                    name=result["name"],
                    known_for_department=result["known_for_department"],
                    movies=movies,
                )
            )

    return creators
