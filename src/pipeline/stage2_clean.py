import re
import unicodedata
from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer


@dataclass
class CleanResult:
    cleaned_text: str
    keywords: list[str]


def stage2_clean(text: str, top_n: int = 10) -> CleanResult:
    cleaned = _normalize(text)
    keywords = _extract_keywords(cleaned, top_n)
    return CleanResult(cleaned_text=cleaned, keywords=keywords)


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _extract_keywords(text: str, top_n: int) -> list[str]:
    raise NotImplementedError("TF-IDF keyword extraction not yet implemented")
