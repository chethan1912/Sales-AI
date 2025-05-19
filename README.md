# 🤖 AI Sales Agent for Forethought

An intelligent, domain-specific Sales Assistant powered by Retrieval-Augmented Generation (RAG) and integrated with a chatbot frontend. This system helps Forethought's sales team provide instant, accurate, and context-aware responses to prospects by leveraging company-specific sales documents and metadata.

## 🚀 Features

- 🔍 **RAG Pipeline**: Combines LLM power with a vector database for precise contextual answers.
- 💬 **Chatbot Frontend**: Built using FastAPI for a clean, responsive interface.
- 🧠 **Embeddings + Chroma DB**: Uses Chroma for embedding-based retrieval of indexed sales knowledge.


---

## 🏗️ Architecture Overview

```plaintext
User Query
   │
   ▼
Chatbot Interface (FastAPI) 
   │
   ▼
Query Preprocessing & Embedding
   │
   ▼
Chroma Vector DB (Retrieval)
   │
   ▼
Context Augmented Prompt
   │
   ▼
LLM (e.g., OpenAI GPT or open-source model)
   │
   ▼
Final Response → User
