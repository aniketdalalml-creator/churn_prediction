from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

reader = PdfReader("docs/sample.pdf")
text = "\n".join(page.extract_text() for page in reader.pages)

chunks = [text[i:i+1000] for i in range(0, len(text), 800)]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)

os.makedirs("vectorstore", exist_ok=True)
faiss.write_index(index, "vectorstore/index.faiss")

with open("vectorstore/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Ingestion complete")
