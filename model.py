from pydantic import BaseModel

class SentimentRequest(BaseModel):
    finnhub_news_id: str
    articleTitle: str
    articleSummary: str

class SentimentResponse(BaseModel):
    finnhub_news_id: str
    score: float