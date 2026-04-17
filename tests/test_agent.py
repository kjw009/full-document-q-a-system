import pytest
from src.agent import run_document_agent


def test_agent_placeholder():
    with pytest.raises(NotImplementedError):
        run_document_agent("What is this document about?")
