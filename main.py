from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import router
from sentiment_analysis import initSentimentAnalysisPipeline

@asynccontextmanager
async def lifespan(app):
    initSentimentAnalysisPipeline()
    yield

app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple API to analyze sentiment using a Hugging Face model.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the Sentiment Analysis API!"}