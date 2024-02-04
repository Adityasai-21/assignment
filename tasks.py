from celery import Celery
from nltk import classify  # Use NLTK for classification
from database import get_session, NewsArticle

app = Celery('tasks')
app.config_from_object('celery_config')

@app.task
def process_article(article):
    # Add your classification logic here
    category = classify(article["content"])

    # Update the database with the assigned category
    session = get_session()
    news_article = session.query(NewsArticle).filter_by(source_url=article["source_url"]).first()
    if news_article:
        news_article.category = category
        session.commit()
    session.close()
