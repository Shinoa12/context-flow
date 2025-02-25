from app.core.config import settings
from pinecone import Pinecone
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import logging

logger = logging.getLogger(__name__)

pc = Pinecone(api_key=settings.PINECONE_API_KEY)
index_name = settings.PINECONE_INDEX
index = pc.Index(index_name)
embedder = OpenAIEmbeddings(model="text-embedding-ada-002")
vector_store = PineconeVectorStore(index=index, embedding=embedder)



def store_text(texts: list, metadatas: list):
    try:
        documents = [Document(page_content=text, metadata=metadata) for text, metadata in zip(texts, metadatas)]
        vector_store.add_documents(documents)
        logger.info("✅ Embeddings almacenados en Pinecone.")
        return True
    except Exception as e:
        logger.error(f"❌ Error al almacenar embeddings: {e}")
        return False

def query_text(query: str, top_k: int = 5):
    try:
        results = vector_store.similarity_search(query, top_k=top_k)
        return results
    except Exception as e:
        logger.error(f"❌ Error al consultar embeddings: {e}")
        return []