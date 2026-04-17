import os
import pathlib
from dotenv import load_dotenv

load_dotenv()

# Paths
ROOT = pathlib.Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
SEED_DIR = DATA_DIR / "seed"
INDEX_DIR = DATA_DIR / "index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)

FAISS_INDEX_PATH = INDEX_DIR / "faiss.index"
TEXTS_PATH = INDEX_DIR / "texts.json"
LABELS_PATH = INDEX_DIR / "labels.json"

# Models
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
SPACY_MODEL = "en_core_web_sm"
CLASSIFIER_MODEL = "distilbert-base-uncased"

# API keys
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

# Document classification rules
DOC_RULES: dict[str, list[str]] = {
    "invoice": ["invoice", "total", "amount due", "bill to", "payment"],
    "news": ["reported", "according to", "said", "announced", "breaking"],
    "contract": ["agreement", "party", "shall", "terms", "obligations", "clause"],
    "regulatory": ["regulation", "compliance", "pursuant", "section", "authority"],
}
