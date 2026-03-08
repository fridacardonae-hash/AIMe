from rag.retriever import retrieve_context
from rag.prompt_builder import build_prompt
from rag.generator import generate_answer

def ask_aime(question):
    context = retrieve_context(question)
    prompt = build_prompt(context, question)
    answer = generate_answer(prompt)
    return answer