from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import logging

logger = logging.getLogger(__name__)

llm = ChatGroq(temperature=0, model_name="llama-3.2-1b-preview")

def generate_humorous_response(query: str, context: str):
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    Eres un gran ayudante que, tomando como contexto {context},
                    intenta responder preguntas de manera humoristica como una persona de la generación Z.
                    O sea, haciendo referencia a memes y cosas así de la cultura popular del internet.
                    """
                ),
                ("human", "{query}")
            ]
        )
        chain = prompt | llm
        response = chain.invoke(
            {
                "context": context,
                "query": query
            }
        )
        
        return response.text()
    except Exception as e:
        logger.error(f"❌ Error al generar respuesta: {e}")
        return "No puedo responder en este momento."