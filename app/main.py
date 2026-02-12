from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="GenAI PDF Q&A")

app.include_router(router)
