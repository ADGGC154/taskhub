from fastapi import FastAPI
import uvicorn

from app.api.v1.auth import router as auth_router
from app.core.config import settings
from app.db.session import engine
import app.models  # noqa: F401  确保模型被加载

app = FastAPI(title=settings.app_name)

app.include_router(auth_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)