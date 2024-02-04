import feedparser

def parse_rss_feeds(rss_feeds):
    articles = []

    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            article = {
                "title": entry.title,
                "content": entry.summary,
                "publication_date": entry.published,
                "source_url": entry.link,
            }
            articles.append(article)

    return articles
