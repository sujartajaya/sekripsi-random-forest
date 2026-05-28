from app.core.settings import settings
import os
import pickle
import numpy as np
from collections import Counter

def bootstrap(X, y):

    n_samples = len(X)

    idx = np.random.choice(
        n_samples,
        n_samples,
        replace=True
    )

    return X[idx], y[idx]


class RandomForest:

    def __init__(
        self,
        n_trees=settings.N_TREES,
        max_depth=settings.MAX_DEPTH,
        min_samples_split=settings.MIN_SAMPLES_SPLIT,
        min_samples_leaf=settings.MIN_SAMPLES_LEAF,
        max_features=settings.MAX_FEATURES,
        criterion=settings.CRITERION,
        random_state=settings.RANDOM_STATE,
        debug=settings.DEBUG
    ):

        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.criterion = criterion
        self.random_state = random_state
        self.debug = debug
        self.is_trained = False
        self.trees = []
        self.accuracy = None                # Tambahan akurasi
        self.precision = None               # Tambahan presisi
        self.recall = None                  # Tambahan recall
        self.dataset_rows = None            # Tambahan data set rows

        if random_state is not None:
            np.random.seed(random_state)

    # Save model
    def save_model(self, model_path=None):
        if not self.is_trained:
            raise RuntimeError("Jalankan fit() terlebih dahulu.")

        if model_path is None:

            folder = MODEL_DIR

            os.makedirs(folder, exist_ok=True)

            model_path = os.path.join(
                folder,
                MODEL_RANDOM_FOREST_FILE
            )

        with open(model_path, 'wb') as f:
            pickle.dump(self, f)
        size_kb = os.path.getsize(model_path) / 1024


        print(f"Model disimpan ke  : {model_path}")
        print(f"Ukuran file        : {size_kb:.1f} KB")
        print(f"Kriteria           : {self.criterion}")
        print(f"Random state       : {self.random_state}")
        print(f"Jumlah pohon       : {len(self.trees)}")
        # Explicitly print the evaluation metrics being saved
        print(f"Accuracy (saat simpan): {self.accuracy:.4f}" if self.accuracy is not None else "Accuracy (saat simpan): None")
        print(f"Precision (saat simpan): {self.precision:.4f}" if self.precision is not None else "Precision (saat simpan): None")
        print(f"Recall (saat simpan): {self.recall:.4f}" if self.recall is not None else "Recall (saat simpan): None")
        print(f"Dataset Rows (saat simpan): {self.dataset_rows}" if self.dataset_rows is not None else "Dataset Rows (saat simpan): None")

        return model_path

    # Load model
    @staticmethod
    def load_model(model_path):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"File tidak ditemukan: {model_path}")
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        if not isinstance(model, RandomForest):
            raise TypeError("Bukan objek RandomForest.")
        print(f"Model dimuat dari  : {model_path}")
        print(f"Jumlah pohon       : {len(model.trees)}")
        print(f"Kriteria           : {model.criterion}")
        print(f"Random state       : {model.random_state}")

        return model

    def fit(self, X, y):

        self.trees = []

        for i in range(self.n_trees):

            if self.debug:
                print("\n################################")
                print(f"MEMBUAT TREE KE-{i+1}")
                print("################################")

            X_sample, y_sample = bootstrap(X, y)

            if self.debug:
                print(f"Bootstrap Sample Shape : {X_sample.shape}")

            tree = DecisionTree(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                min_samples_leaf=self.min_samples_leaf,
                max_features=self.max_features,
                criterion=self.criterion,
                debug=self.debug
            )

            tree.fit(X_sample, y_sample)

            self.trees.append(tree)

        if self.debug:
            print("\n================================")
            print("SEMUA TREE BERHASIL DIBUAT")
            print("================================")

        self.is_trained = True

    def predict(self, X):

        predictions = np.array([
            tree.predict(X)
            for tree in self.trees
        ])

        predictions = predictions.T

        final_predictions = []

        for row in predictions:

            counter = Counter(row)
            final_predictions.append(
                counter.most_common(1)[0][0]
            )

        return np.array(final_predictions)


    # Tambahan feature importance
    def feature_importances(self, X, y, n_permutations=5):
        """Permutation importance: drop in accuracy ketika fitur di-shuffle."""
        baseline = np.mean(self.predict(X) == y)
        importances = np.zeros(X.shape[1])
        rng = np.random.default_rng(self.random_state)

        for feat in range(X.shape[1]):
            scores = []
            for _ in range(n_permutations):
                X_perm = X.copy()
                X_perm[:, feat] = rng.permutation(X_perm[:, feat])
                score = np.mean(self.predict(X_perm) == y)
                scores.append(score)
            importances[feat] = baseline - np.mean(scores)

        return importances

    # Probabilitas
    def predict_proba(self, X):

        # ambil prediksi semua tree
        tree_preds = np.array([
            tree.predict(X)
            for tree in self.trees
        ])

        # rata-rata vote
        prob_class1 = np.mean(tree_preds, axis=0)

        # probabilitas class 0
        prob_class0 = 1 - prob_class1

        # gabungkan
        probabilities = np.column_stack([
            prob_class0,
            prob_class1
        ])

        return probabilities