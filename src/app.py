from fastapi import FastAPI
from src.api import api_router
from src.auth.endpoints import router as auth_router


def create_app():
    _app = FastAPI(
        name="Go Algo",
        description="Hackathon API",
    )
    _app.include_router(api_router)
    _app.include_router(auth_router)
    return _app
