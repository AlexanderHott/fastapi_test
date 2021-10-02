"""
https://www.youtube.com/watch?v=kCggyi_7pHg
"""
from fastapi import FastAPI  # pip install fastapi
from pydantic import BaseModel
import requests
import typing as t

app = FastAPI()

db: list[dict[str, str]] = []


class City(BaseModel):
    """Basic City dataclass"""

    name: str
    timezone: str


@app.get("/")
def index() -> None:
    """API test"""
    return {"key": "value"}


@app.get("/cities/")
def get_cities() -> list[dict[str, str]]:
    """Get all of the cities"""
    results = []
    for city in db:
        r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
        current_time = r.json()["datetime"]
        results.append(
            {
                "name": city["name"],
                "timezone": city["timezone"],
                "current_time": current_time,
            }
        )
    return db


@app.get("/cities/{city_id}")
def get_city(city_id: int) -> dict[str, str]:
    """Get a specific city"""
    return db[city_id - 1]


@app.post("/cities")
def create_city(city: City) -> dict[str, str]:
    """Add a city"""
    db.append(city.dict())
    return db[-1]


@app.delete("/cities/{city_id}")
def delete_city(city_id: int):
    """Delete a city"""
    db.pop(city_id - 1)
    return dict()


# uvicorn main:app --reload
