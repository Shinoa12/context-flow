from app.services.langchain_service import generate_humorous_response
from app.services.pinecone_service import query_text
import logging

logger = logging.getLogger(__name__)

def test_humorous_response():
    try:
        query = "Habrá algun efecto climatico absurdo?"
        response = query_text(query, top_k=5)
        context = " ".join([res.page_content for res in response])
        humorous_response = generate_humorous_response(query, context)

        print(humorous_response)
        print(response[0].metadata.get("url", "https://example.com"))
        assert response is not None
    except Exception as e:
        logger.error(f"❌ Error al generar respuesta: {e}")

test_humorous_response()