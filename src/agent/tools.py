from src.store import store


def search_documents(query: str, top_k: int = 5) -> list[dict]:
    """Semantic search over the FAISS store. Returns top_k matching chunks."""
    return store.search(query, top_k=top_k)


def get_documents_by_label(label: str) -> list[str]:
    """Return all document texts with a given doc_type label."""
    return [t for t, l in zip(store.texts, store.labels) if l == label]


def list_entities(text: str) -> list[dict]:
    """Run NER on a text snippet and return entity dicts."""
    from src.pipeline.stage3_ner import stage3_ner
    return stage3_ner(text)
