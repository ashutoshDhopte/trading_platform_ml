from pydantic import BaseModel

class SentimentRequest(BaseModel):
    articleTitle: str
    articleSummary: str

class SentimentResponse(BaseModel):
    articleTitle: str
    score: float