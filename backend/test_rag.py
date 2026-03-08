from rag.rag_pipeline import ask_aime

while True:
    question = input("\nAsk AIMe something: ")
    if question == "exit":
        break
    response = ask_aime(question)
    print("\nAIMe:\n")
    print(response)