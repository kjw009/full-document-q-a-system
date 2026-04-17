import pathlib


def stage1_ocr(file_path: str, source: str = "text") -> str:
    path = pathlib.Path(file_path)
    if source == "text":
        return _read_text(path)
    elif source == "pdf":
        return _read_pdf(path)
    elif source == "image":
        return _read_image(path)
    else:
        raise ValueError(f"Unknown OCR source: {source!r}")


def _read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def _read_pdf(path: pathlib.Path) -> str:
    raise NotImplementedError("PDF extraction not yet implemented")


def _read_image(path: pathlib.Path) -> str:
    raise NotImplementedError("Image OCR not yet implemented")
