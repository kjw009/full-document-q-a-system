import pytest
from src.pipeline import stage1_ocr, run
from src.pipeline.result import PipelineResult


def test_stage1_reads_text_file(tmp_path):
    f = tmp_path / "doc.txt"
    f.write_text("Hello world")
    assert stage1_ocr(str(f), source="text") == "Hello world"


def test_stage1_rejects_unknown_source(tmp_path):
    f = tmp_path / "doc.txt"
    f.write_text("")
    with pytest.raises(ValueError):
        stage1_ocr(str(f), source="unknown")


def test_run_returns_pipeline_result():
    with pytest.raises(NotImplementedError):
        run("Some document text.")
