from .faiss_store import FaissStore

store = FaissStore()
embedder = store.embedder
index = store.index
texts = store.texts
labels = store.labels
