from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.util.text_processing import clean_text
from app.services.pinecone_service import query_text
from app.services.langchain_service import generate_humorous_response
from app.core.logging_config import setup_logging

setup_logging()

app =  FastAPI(title="Lucy Humoristic QnA")

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    link: str

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(question: str) -> str:
    clean_question = clean_text(question)

    results = query_text(clean_question)
    if not results:
        return HTTPException(status_code=404, detail="Sorry, no results found :(")
    
    context = " ".join([res.page_content for res in results])
    best_link = results[0].metadata.get("url", "https://example.com")

    humorous_response = generate_humorous_response(clean_question, context)

    return AnswerResponse(answer=humorous_response, link=best_link)