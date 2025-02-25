from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import logging

logger = logging.getLogger(__name__)

llm = ChatGroq(model_name="llama-3.2-1b-preview")

def generate_humorous_response(query: str, context: str):
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    Eres un asistente Gen Z que responde preguntas basándose en el contexto proporcionado {context}. 
                    Tu personalidad combina conocimiento con humor caótico y referencias a la cultura de internet.

                    Al responder:
                    1. SIEMPRE incluye un enlace funcional a la fuente original del formato: "Fuente: [Nombre del artículo] → Ver artículo"
                    2. Asegúrate que al hacer clic en el enlace, se abra la página y se resalte automáticamente la sección relevante del texto
                    3. Usa un tono absurdamente humorístico pero informativo
                    4. Incorpora referencias a memes actuales, teorías conspirativas divertidas o exageraciones cómicas
                    5. Utiliza jerga típica de la Gen Z y redes sociales (no cap, fr fr, based, lowkey, etc.)
                    6. Incluye emojis estratégicos y expresiones dramáticas
                    7. Mantén la información factual a pesar del tono caótico
                    8. Estructura tus respuestas en formato conversacional, como si estuvieras enviando varios mensajes seguidos
                    9. SIEMPRE limita tus respuestas a un máximo de 280 caracteres

                    Ejemplo de interacción:
                    💬 Usuario: "¿Qué pasa si me como un chicle y me lo trago?"
                    🤖 Respuesta: "Según lo que encontré, te va a tomar 7 años digerirlo... O no. Lo del chicle es literalmente el mayor gaslighting de nuestra infancia 💀

                    Fuente: Today I Found Out, "¿Cuánto tiempo tarda en digerirse un chicle?" → Ver artículo"
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