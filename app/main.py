from fastapi import FastAPI
import uvicorn

from app.core.config import settings
from app.db.session import engine

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)