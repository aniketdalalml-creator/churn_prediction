from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL

def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)
