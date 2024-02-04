from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = "news_articles"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    publication_date = Column(DateTime, nullable=False)
    source_url = Column(String, nullable=False, unique=True)
    category = Column(String)  # Add category column

def create_database(engine):
    Base.metadata.create_all(engine)

def insert_articles(session, articles):
    for article_data in articles:
        article = NewsArticle(**article_data)
        try:
            session.add(article)
            session.commit()
        except IntegrityError:
            session.rollback()

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
