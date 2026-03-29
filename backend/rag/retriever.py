import os
import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent



DOCKER_MODEL_PATH = Path("/app/models/all-MiniLM-L6-v2")

if DOCKER_MODEL_PATH.exists():
    MODEL_PATH = DOCKER_MODEL_PATH
    transcripts_folder = Path("/app/backend//db/transcripts")
    embeddings_folder = Path("/app/backend/db/embeddings")
else:
    MODEL_PATH = "all-MiniLM-L6-v2"
    transcripts_folder = BASE_DIR / "backend" / "db" / "transcripts"
    embeddings_folder = BASE_DIR / "backend" / "db" / "embeddings"


model = None
index = None
documents = None
resources_loaded = False


def load_resources():
    global model, index, documents, resources_loaded

    if resources_loaded:
        return
    model = SentenceTransformer(str(MODEL_PATH))
    index = faiss.read_index(str(embeddings_folder / "aime_index1.1.faiss"))

    files = sorted(
        [f for f in transcripts_folder.iterdir() if f.name.endswith("_en.txt")],
        key=lambda x: x.name
    )
    documents = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            documents.append(f.read())

    resources_loaded = True


def retrieve_context(question, k=5):

    load_resources()

    question_embedding = model.encode([question])
    faiss.normalize_L2(question_embedding)
    distances, indices = index.search(np.array(question_embedding), k)

    context = ""
    for i in indices[0]:
        context += documents[i] + "\n\n"
        print("DOC:", documents[i][:200])

    return context