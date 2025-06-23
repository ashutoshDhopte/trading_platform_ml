import fastapi
from typing import List
from model import SentimentRequest, SentimentResponse
import sentiment_analysis

router = fastapi.APIRouter(prefix="/sentiment", tags=["Sentiment"])

@router.post(
        "/analyze",
        response_model=List[SentimentResponse]
)
def analyze_sentiment(request: List[SentimentRequest]):

    sentimentResponse: List[SentimentResponse] = []
    
    print(f"Analyzing text: '{request}'")

    result = sentiment_analysis.analyze(request)
    for req, res in zip(request, result):
        print(res)
        score = res['score']
        if res['label'] == 'negative':
            score *= -1
        sentimentResponse.append(SentimentResponse(
            finnhub_news_id=req.finnhub_news_id,
            score=score
        ))
    
    return sentimentResponse