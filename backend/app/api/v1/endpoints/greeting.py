from fastapi import APIRouter
from app.schemas.greeting import Greeting

router = APIRouter()

@router.get("/", response_model=Greeting)
def read_greeting():
    return Greeting(message="Hello from the backend!")
