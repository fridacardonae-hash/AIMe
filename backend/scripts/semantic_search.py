import faiss
import os 
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

transcripts_folder = BASE_DIR / "backend" / "db" / "transcripts"
embeddings_folder = BASE_DIR / "backend" / "db" / "embeddings"
index_path = embeddings_folder / "aime_index.faiss"

print("Loading embedding model...")
print("basedir:", BASE_DIR)
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Loading FAISS index...")
index = faiss.read_index(str(index_path))
print("FAISS index loaded.")

documents = []

for file in os.listdir(transcripts_folder):
    if file.endswith("_en.txt"):
        with open(os.path.join(transcripts_folder, file), "r", encoding="utf-8") as f:
            documents.append(f.read())

while True:
    question = input("\n Ask AIMe something: ")
    if question == "exit":
        break
    question_embedding = model.encode([question])
    k = 3
    distances, indices = index.search(np.array(question_embedding),k)
    print("\nMost relevant documents:")

    for i in indices[0]:
        print(documents[i])
        print("\n----------------------\n")

