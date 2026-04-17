from .stage1_ocr import stage1_ocr
from .result import PipelineResult
from .stage2_clean import stage2_clean
from .stage3_ner import stage3_ner
from .stage4_classify import stage4_classify


def run(raw_text: str) -> PipelineResult:
    cleaned = stage2_clean(raw_text)
    entities = stage3_ner(cleaned.cleaned_text)
    doc_type = stage4_classify(cleaned.cleaned_text)
    return PipelineResult(
        raw_text=raw_text,
        cleaned_text=cleaned.cleaned_text,
        keywords=cleaned.keywords,
        entities=entities,
        doc_type=doc_type,
    )
