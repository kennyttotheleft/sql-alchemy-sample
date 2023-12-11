# coding=utf-8

from fastapi import Depends, FastAPI

from backend.routers import user_router

app = FastAPI()
app.include_router(user_router.router)

@app.get("/")
def get_root() -> dict:
    return {"Hello": "World"}
