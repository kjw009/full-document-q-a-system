from src import pipeline
from src.agent import run_document_agent
from src.store import embedder, index, labels, texts


def document_qa_system(file_path: str, question: str, ocr_engine: str = "text") -> str:
    # Stage 1: Get raw text via OCR (or direct if already text)
    raw_text = pipeline.stage1_ocr(file_path, source=ocr_engine)

    # Stages 2-5: Run the full NLP pipeline
    result = pipeline.run(raw_text)

    # Add to the FAISS vector store
    embedding = embedder.encode([result.cleaned_text], normalize_embeddings=True)
    index.add(embedding.astype("float32"))
    texts.append(result.cleaned_text)
    labels.append(result.doc_type)

    # Use the agent to answer the question
    answer = run_document_agent(question, verbose=False)
    return answer
