import pickle

from app.ml.algorithms.random_forest import RandomForest
from app.ml.algorithms.decision_tree import DecisionTree

OLD_MODEL = "app/ml/models/random_forest_old.pkl"
NEW_MODEL = "app/ml/models/random_forest_manual_v1.pkl"


# load model lama
with open(OLD_MODEL, "rb") as f:
    model = pickle.load(f)


# save ulang
with open(NEW_MODEL, "wb") as f:
    pickle.dump(model, f)


print("Model berhasil disave ulang")