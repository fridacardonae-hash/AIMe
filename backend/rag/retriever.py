import os
import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent
transcripts_folder = BASE_DIR / "backend" / "db" / "transcripts"
embeddings_folder = BASE_DIR / "backend" / "db" / "embeddings"

DOCKER_MODEL_PATH = Path("/app/models/all-MiniLM-L6-v2")

if DOCKER_MODEL_PATH.exists():
    MODEL_PATH = DOCKER_MODEL_PATH
else:
    MODEL_PATH = "all-MiniLM-L6-v2"


model = None
index = None
documents = None
resources_loaded = False


def load_resources():
    global model, index, documents, resources_loaded

    if resources_loaded:
        return
    model = SentenceTransformer(str(MODEL_PATH))
    index = faiss.read_index(str(embeddings_folder / "aime_index.faiss"))

    files = sorted(
        [f for f in transcripts_folder.iterdir() if f.name.endswith("_en.txt")],
        key=lambda x: x.name
    )
    documents = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            documents.append(f.read())

    resources_loaded = True


def retrieve_context(question, k=3):

    load_resources()

    question_embedding = model.encode([question])
    distances, indices = index.search(np.array(question_embedding), k)

    context = ""
    for i in indices[0]:
        context += documents[i] + "\n\n"

    return context