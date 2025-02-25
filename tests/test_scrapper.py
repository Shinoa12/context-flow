import logging
from app.scraper.article_scraper import get_unusual_articles_urls, get_article_content
from app.services.chunking_service import chunk_text
from app.services.pinecone_service import store_text
from app.services.metadata_service import generate_metadata

logger = logging.getLogger(__name__)

def test_scrape():
    try:
        content = get_article_content("https://en.wikipedia.org/wiki/Meaning_of_life")
        print(content["title"])
        print(content["content"])
    except Exception as e:
        logger.error(f"❌ Error al obtener el contenido: {e}")

def scrape_and_store_articles():
    try:
        with open('../context-flow/links.txt', 'r') as file:
            # Lee todas las líneas y elimina los saltos de línea
            urls = [line.strip() for line in file]

        for url in urls:
            article_dict = get_article_content(url)
            chunks = chunk_text(article_dict["content"])
            metadata = generate_metadata(url, article_dict["title"], chunks)
            store_text(chunks, metadata)
            logger.info(f"✅ Se ha almacenado el artículo: {article_dict['title']}")
        
        logger.info("✅ Se han almacenado los artículos en Pinecone.")
    
    except Exception as e:
        logger.error(f"❌ Error al almacenar los artículos: {e}")


scrape_and_store_articles()