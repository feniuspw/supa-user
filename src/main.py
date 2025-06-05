import logging
from fastapi import FastAPI
from api import auth

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

app.include_router(auth.router)
