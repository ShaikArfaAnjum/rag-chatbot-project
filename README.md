<<<<<<< HEAD
# rag-chatbot-project
RAG-based chatbot using FAISS and Sentence Transformers
=======
# RAG-Based AI Chatbot

## Objective
Build a question-answering assistant that retrieves answers from custom documents using SentenceTransformer embeddings and FAISS.

## How it Works
1. Load and split text documents from `txt_docs/`.
2. Convert text chunks into embeddings using SentenceTransformer.
3. Store embeddings in FAISS vector store.
4. User query is embedded and searched for relevant documents.
5. Chatbot returns the answer in CLI.

## Usage
1. Install dependencies:
```bash
pip install -r requirements.txt
>>>>>>> 2166072 (Initial commit: RAG-based chatbot project)
