import json

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from src.config import (
    EMBEDDING_MODEL,
    FAISS_INDEX_PATH,
    LABELS_PATH,
    TEXTS_PATH,
)


class FaissStore:
    def __init__(self):
        self.embedder = SentenceTransformer(EMBEDDING_MODEL)
        self.texts: list[str] = []
        self.labels: list[str] = []
        self.index: faiss.IndexFlatIP = faiss.IndexFlatIP(384)
        self._load_if_exists()

    def add(self, text: str, label: str) -> None:
        embedding = self.embedder.encode([text], normalize_embeddings=True)
        self.index.add(embedding.astype("float32"))
        self.texts.append(text)
        self.labels.append(label)

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        raise NotImplementedError("FAISS search not yet implemented")

    def save(self) -> None:
        raise NotImplementedError("FAISS save not yet implemented")

    def _load_if_exists(self) -> None:
        if FAISS_INDEX_PATH.exists() and TEXTS_PATH.exists() and LABELS_PATH.exists():
            raise NotImplementedError("FAISS load not yet implemented")
