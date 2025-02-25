import requests
from app.scraper.article_scraper import get_unusual_articles_urls, get_article_content

urls = get_unusual_articles_urls()
#print(urls)

test_url = urls[1]
article = get_article_content(test_url)

print(article["title"])
print(article["content"][:1000])