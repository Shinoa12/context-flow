from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from app.core.config import settings
import logging
import os

logger = logging.getLogger(__name__)

os.environ["GROQ_API_KEY"] = settings.GROQ_API_KEY

if "GROQ_API_KEY" not in os.environ:
    raise ValueError("La variable de entorno GROQ_API_KEY no está definida.")

llm = ChatGroq(model_name="llama-3.2-1b-preview")

def generate_humorous_response(query: str, context: str):
    try:
        # Crear el prompt usando from_template()
        prompt = ChatPromptTemplate.from_template(
            """
            DOCUMENT: 
            {context}

            QUESTION: 
            {query}

            INSTRUCTIONS: 
            Answer the user's QUESTION using the DOCUMENT text above.
            - Keep your answer grounded in the facts of the DOCUMENT.
            - Answer in a chaotic and humorous Gen Z style with sarcastic jokes, meme references, and over-the-top humor.
            - Use Gen Z slang (no cap, fr fr, based, lowkey, vibe check, etc.) and strategically placed emojis (👽💀🔥👀).
            - Break your answer into multiple short messages, like a real chat conversation.
            - Maintain your answer short and sweet, with a maximum of 280 characters per message.
            - ALWAYS include the url to the Wikipedia article of the information in the last message.
            """
        )

        # Crear el chain usando LLMChain
        chain = LLMChain(llm=llm, prompt=prompt)

        # Ejecutar el chain con las variables de contexto y query
        response = chain.run({
            "context": context,
            "query": query
        })
        
        return response
    except Exception as e:
        logger.error(f"❌ Error al generar respuesta: {e}")
        return "No puedo responder en este momento."