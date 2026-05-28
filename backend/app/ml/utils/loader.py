from app.ml.algorithms.random_forest import RandomForest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "random_forest_manual_v2.pkl"

_model_cache = None


def get_model():

    global _model_cache

    if _model_cache is None:
        _model_cache = RandomForest.load_model(MODEL_PATH)

    return _model_cache


def get_model_info():

    model = get_model()

    return {
        "model_type": type(model).__name__,
        "n_trees": getattr(model, "n_trees", None),
        "max_depth": getattr(model, "max_depth", None),
        "min_samples_split": getattr(model, "min_samples_split", None),
        "max_features": getattr(model, "max_features", None),
        "criterion": getattr(model, "criterion", None),
        "random_state": getattr(model, "random_state", None),
        # tambahan baru
        "accuracy": getattr(model, "accuracy", None),
        "precision": getattr(model, "precision", None),
        "recall": getattr(model, "recall", None),
        "dataset_rows": getattr(model, "dataset_rows", None),
    }