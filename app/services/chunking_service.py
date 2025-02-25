import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

def chunk_text(content: str):
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_text(content)
        
        logger.info(f"✅ Se han generado {len(chunks)} chunks.")
        return chunks
    
    except Exception as e:
        logger.error(f"❌ Error en el chunking del contenido: {e}")
        return []