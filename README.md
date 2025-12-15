<<<<<<< HEAD
# rag-chatbot-project
RAG-based chatbot using FAISS and Sentence Transformers
=======
# RAG-Based AI Chatbot

z

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

##Safety & Guardrails
Runs fully offline to prevent data leakage
No external API calls or cloud dependency
Environment variables used for sensitive values
Limits response length to avoid hallucinations
Returns only retrieved document content

##Results
Successfully retrieves relevant text chunks
Produces concise and accurate answers
Fast response time due to FAISS indexing
Works with multiple text files simultaneously

##Future Improvements
Add LLM-based answer refinement
Introduce relevance score filtering
Add document upload support
Implement multi-agent orchestration
Extend UI from CLI to web interface

##Conclusion
Demonstrates a complete local RAG pipeline
Highlights efficient document retrieval using embeddings
Serves as a foundation for advanced Agentic AI systems
Aligns with best practices in modern AI application design
