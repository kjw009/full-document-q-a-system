"""Exercise 4: Plot precision/recall/F1 per entity type."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def plot_entity_metrics(predictions: list[dict], ground_truth: list[dict]):
    raise NotImplementedError("Evaluation dashboard not yet implemented")


if __name__ == "__main__":
    plot_entity_metrics([], [])
