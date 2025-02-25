import logging
from app.scraper.article_scraper import get_unusual_articles_urls, get_article_content
from app.services.chunking_service import chunk_text
from app.services.pinecone_service import store_text
from app.services.metadata_service import generate_metadata

logger = logging.getLogger(__name__)

def scrape_and_store_articles():
    try:
        urls = get_unusual_articles_urls()

        for url in urls:
            article_dict = get_article_content(url)
            chunks = chunk_text(article_dict["content"])
            metadata = generate_metadata(url, article_dict["title"], chunks)
            store_text(chunks, metadata)
        
        logger.info("✅ Se han almacenado los artículos en Pinecone.")
    
    except Exception as e:
        logger.error(f"❌ Error al almacenar los artículos: {e}")


scrape_and_store_articles()