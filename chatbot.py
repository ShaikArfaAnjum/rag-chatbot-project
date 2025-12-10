import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import nltk

# Download punkt if not already
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# ----------- Load TXT files ----------
def load_text_files(folder_path="txt_docs"):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            path = os.path.join(folder_path, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    documents.append(text)
    return documents

# ----------- Split documents ----------
def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ----------- Limit output to 4 sentences ----------
def summarize_to_4_sentences(text):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:4])

# ----------- Main chatbot ----------
def main():
    print("Chatbot is ready! Type your question.")
    print("Type 'exit' to quit.\n")

    folder = "txt_docs"
    documents = load_text_files(folder)
    if not documents:
        print("❌ No .txt files found or empty in", folder)
        return

    # Split into chunks
    all_chunks = []
    for doc in documents:
        all_chunks.extend(split_text(doc))

    # Embeddings
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(all_chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break

        # Get top 3 relevant chunks
        query_vec = model.encode([query]).astype("float32")
        D, I = index.search(query_vec, k=3)

        # Combine top chunks
        combined_text = " ".join([all_chunks[idx] for idx in I[0]])
        # Summarize to max 4 sentences
        answer = summarize_to_4_sentences(combined_text)

        print("\nBot (max 4 sentences):")
        print(answer)
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()
