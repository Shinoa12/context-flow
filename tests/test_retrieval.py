from app.services.pinecone_service import query_text
from app.services.pinecone_service import index
from app.services.pinecone_service import embedder
import logging

logger = logging.getLogger(__name__)

def test_humorous_response():
    try:
        query = "Death"
        #print(query_vector)
        results = query_text(query, top_k=10)
        #print(results)

        for res in results:
            print(res.metadata.get("url", "https://example.com"))

        #assert results is not None
    except Exception as e:
        logger.error(f"❌ Error al generar respuesta: {e}")

test_humorous_response()