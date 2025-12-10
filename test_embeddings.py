from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example: embed a list of sentences
sentences = ["Hello world!"]
vectors = model.encode(sentences)

print("Embedding shape:", vectors.shape)  # Should print (1, 384)
