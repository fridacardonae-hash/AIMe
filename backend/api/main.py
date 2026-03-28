from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag.rag_pipeline import ask_aime
from rag.retriever import load_resources
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_resources()
    print("Model and documents loaded")
    yield
    print("Shutting down")

app = FastAPI(
    title="AIMe API",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

@app.get("/")
def root():
    return {"status": "AIMe API running."}

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(question: Question):
    response = ask_aime(question.question)
    return {
        "answer": response
        }