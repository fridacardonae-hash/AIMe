import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent

transcripts_folder = BASE_DIR / "backend" / "db" / "transcripts"
embeddings_folder = BASE_DIR / "backend" / "db" / "embeddings"

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index(str(embeddings_folder / "aime_index.faiss"))

documents = []

for file in transcripts_folder.iterdir():
    if file.name.endswith("_en.txt"):
        with open(file, "r", encoding="utf-8") as f:
            documents.append(f.read())

def retrieve_context(question, k=3):
    question_embedding = model.encode([question])
    distances, indices = index.search(np.array(question_embedding), k)

    context = ""
    for i in indices[0]:
        context += documents[i] + "\n\n"
    
    return context