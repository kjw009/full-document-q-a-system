from dataclasses import dataclass, field


@dataclass
class PipelineResult:
    raw_text: str
    cleaned_text: str
    keywords: list[str]
    entities: list[dict]  # [{"text": ..., "label": ...}]
    doc_type: str
