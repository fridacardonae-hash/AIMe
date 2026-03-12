from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag.rag_pipeline import ask_aime

app = FastAPI(title="AIMe API")

@app.get("/")
def root():
    return {"status": "AIMe API running."}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(question: Question):
    response = ask_aime(question.question)
    return {
        "answer": response
        }