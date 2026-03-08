import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

transcripts_folder = BASE_DIR / "backend" / "db" / "transcripts"
embeddings_folder = BASE_DIR / "backend" / "db" / "embeddings"


os.makedirs(embeddings_folder, exist_ok=True)   

print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

documents = []
filenames = []

for file in os.listdir(transcripts_folder):
    if file.endswith("_en.txt"):
        path = os.path.join(transcripts_folder, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

            documents.append(text)
            filenames.append(file)

print("Creating embeddings...")
embeddings = model.encode(documents, show_progress_bar=True)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, os.path.join(embeddings_folder, "aime_index.faiss"))

print("Embeddings created and index saved.")