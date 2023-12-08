from fastapi import Depends, FastAPI

app = FastAPI()

async def _get_detail() -> str:
    return "detail-info"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(
    item_id: int,
    q: str = None,
    detail: str = Depends(_get_detail),
):
    return {"item_id": item_id, "q": q, "detail": detail}