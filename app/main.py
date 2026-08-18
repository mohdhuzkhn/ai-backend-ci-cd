import os

from fastapi import FastAPI

app = FastAPI(title="AI Backend API")


@app.get("/")
def read_root():
    return {"status": "online", "service": "AI Backend"}


@app.get("/health")
def health_check():
    db_host = os.getenv("POSTGRES_HOST", "localhost")
    redis_host = os.getenv("REDIS_HOST", "localhost")

    return {
        "postgres_configured": bool(db_host),
        "redis_configured": bool(redis_host),
    }
