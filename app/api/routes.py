from fastapi import APIRouter
from app.models.schemas import QuestionRequest, AnswerResponse
from app.services.qa_service import answer_question

router = APIRouter()

@router.post("/ask", response_model=AnswerResponse)
def ask(payload: QuestionRequest):
    answer = answer_question(payload.question)
    return {"answer": answer}
