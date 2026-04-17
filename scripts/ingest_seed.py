"""Batch-ingest all files in data/seed/ into the FAISS store."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import pipeline
from src.store import store


def ingest_all():
    seed_dir = Path(__file__).parent.parent / "data" / "seed"
    files = list(seed_dir.iterdir())
    if not files:
        print("No seed files found. Add documents to data/seed/ first.")
        return

    for path in files:
        print(f"Ingesting {path.name}...")
        suffix = path.suffix.lower()
        source = "pdf" if suffix == ".pdf" else "image" if suffix in {".png", ".jpg", ".jpeg"} else "text"
        raw_text = pipeline.stage1_ocr(str(path), source=source)
        result = pipeline.run(raw_text)
        store.add(result.cleaned_text, result.doc_type)
        print(f"  -> doc_type={result.doc_type}, entities={len(result.entities)}")

    store.save()
    print(f"Done. {len(store.texts)} documents in store.")


if __name__ == "__main__":
    ingest_all()
