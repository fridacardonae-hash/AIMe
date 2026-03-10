# AIMe — AI Portfolio Assistant 🤖

**AIMe** is an AI-powered assistant designed to answer questions about my professional experience, projects, and technical background as a **Mechatronics Engineer**.

Instead of reading a traditional résumé, visitors can **interact with an AI that represents me**, asking questions about my work, projects, and skills.

The system uses a **Retrieval-Augmented Generation (RAG)** pipeline to retrieve relevant information from a knowledge base built from transcripts of my experiences and projects.

---

#  Features

- Conversational **AI portfolio interface**
- **Retrieval-Augmented Generation (RAG)**
- Semantic search using **vector embeddings**
- **FastAPI backend** for AI inference
- **React + TypeScript frontend**
- **FAISS vector database** for similarity search
- Integration with **OpenAI API**
- Responsive UI inspired by modern chat interfaces

---

---
##  Project Structure

```
AIMe
│
├── frontend
│   ├── src
│   │   ├── components
│   │   │   ├── Chat.tsx
│   │   │   ├── Message.tsx
│   │   │   └── Sidebar.tsx
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── styles.css
│   │
│   ├── index.html
│   └── package.json
│
├── backend
│   ├── api
│   │   └── main.py
│   │
│   ├── rag
│   │   ├── generator.py
│   │   ├── rag_pipeline.py
│   │   └── prompt_builder.py
│   │
│   ├── scripts
│   │   └── building_embeddings.py
│   │
│   └── db
│       ├── transcripts
│       └── embeddings
│
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

## Frontend

- **React**
- **TypeScript**
- **Vite**
- **CSS**

## Backend

- **FastAPI**
- **Python**
- **FAISS**
- **OpenAI API**

## AI / ML

- **Retrieval-Augmented Generation (RAG)**
- **Semantic embeddings**
- **Vector similarity search**

---
---

#  How the RAG System Works

1. Experience transcripts are stored in `/db/transcripts`.
2. The script `building_embeddings.py` generates vector embeddings.
3. Embeddings are stored in a **FAISS index**.
4. When a user asks a question:

- The system retrieves relevant context.
- A prompt is constructed using the retrieved information.
- The LLM generates a response grounded in that context.

This ensures answers are **based on real experience instead of hallucinations**.

---

# 🌐 Deployment

The application is designed to be deployed using:

**Frontend**
- Vercel

**Backend**
- Render

Environment variables are used to securely store API keys.

---

# 👩‍💻 About Me

Hi! I'm **Frida Cardona**, a **Mechatronics Engineer** passionate about:

- Artificial Intelligence
- Computer Vision
- Automation
- Embedded Systems
- Manufacturing Technology

This project explores transforming a traditional résumé into an **interactive AI experience**.

---

# 📬 Contact

**LinkedIn**  
https://www.linkedin.com/in/frida-cardona-810858202/

**GitHub**  
https://github.com/frida-cardona-hash
