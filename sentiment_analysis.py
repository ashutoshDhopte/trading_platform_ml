from typing import List
from transformers import pipeline
from model import SentimentRequest

sentiment_pipeline = None

def initSentimentAnalysisPipeline():
    global sentiment_pipeline
    sentiment_pipeline = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
    print("Sentiment analysis model initialized")

def analyze(sentimentRequestList: List[SentimentRequest]) -> list[dict]:
    if sentiment_pipeline is not None:
        articleTexts = []
        for req in sentimentRequestList:
            # Concatenate title and summary for sentiment analysis
            articleTexts.append(req.articleTitle + ". " + req.articleSummary)
        if len(articleTexts) > 0:
            return sentiment_pipeline(articleTexts)
    return []

