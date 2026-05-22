import numpy as np

def calculate_impurity(y, criterion='gini'):

    classes = np.unique(y)

    if criterion == 'gini':

        impurity = 1

        for cls in classes:

            p = np.sum(y == cls) / len(y)

            impurity -= p ** 2

        return impurity

    elif criterion == 'entropy':

        entropy = 0

        for cls in classes:

            p = np.sum(y == cls) / len(y)

            if p > 0:
                entropy -= p * np.log2(p)

        return entropy


def split_data(X, y, feat, threshold):

    values = X[:, feat]

    left_mask = values <= threshold
    right_mask = values > threshold

    X_left = X[left_mask]
    y_left = y[left_mask]

    X_right = X[right_mask]
    y_right = y[right_mask]

    return X_left, y_left, X_right, y_right


def best_split(
    X,
    y,
    min_samples_leaf=1,
    max_features='sqrt',
    criterion='gini'
):

    best_impurity = 999
    best_feat = None
    best_threshold = None

    n_features = X.shape[1]

    # feature selection random forest
    if max_features == 'sqrt':

        k = max(1, int(np.sqrt(n_features)))

    elif max_features == 'log2':

        k = max(1, int(np.log2(n_features)))

    elif isinstance(max_features, int):

        k = min(max_features, n_features)

    else:

        k = n_features

    feat_idxs = np.random.choice(
        n_features,
        k,
        replace=False
    )

    for feat in feat_idxs:

        values = X[:, feat]

        thresholds = np.unique(values)

        for threshold in thresholds:

            X_left, y_left, X_right, y_right = split_data(
                X, y, feat, threshold
            )

            # min samples leaf
            if len(y_left) < min_samples_leaf:
                continue

            if len(y_right) < min_samples_leaf:
                continue

            impurity_left = calculate_impurity(
                y_left,
                criterion
            )

            impurity_right = calculate_impurity(
                y_right,
                criterion
            )

            weighted_impurity = (
                len(y_left) * impurity_left +
                len(y_right) * impurity_right
            ) / len(y)

            if weighted_impurity < best_impurity:

                best_impurity = weighted_impurity
                best_feat = feat
                best_threshold = threshold

    return best_feat, best_threshold, best_impurity


def leaf_value(y):

    counter = Counter(y)

    return counter.most_common(1)[0][0]


class DecisionTree:

    def __init__(
        self,
        max_depth=5,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features='sqrt',
        criterion='gini',
        debug=False
    ):

        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.criterion = criterion
        self.debug = debug

        self.tree = None

    def fit(self, X, y):

        if self.debug:
            print("\n==============================")
            print("MEMULAI PEMBUATAN DECISION TREE")
            print("==============================")

        self.tree = self.build_tree(X, y)

    def build_tree(self, X, y, depth=0):

        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))

        if self.debug:
            print(f"\nDepth              : {depth}")
            print(f"Jumlah Sample      : {n_samples}")
            print(f"Jumlah Class       : {n_classes}")

        # kondisi stop
        if (
            depth >= self.max_depth or
            n_classes == 1 or
            n_samples < self.min_samples_split
        ):

            leaf = leaf_value(y)

            if self.debug:
                print(">> Membuat LEAF")
                print(f">> Nilai leaf      : {leaf}")

            return leaf

        feat, threshold, impurity = best_split(
            X,
            y,
            min_samples_leaf=self.min_samples_leaf,
            max_features=self.max_features,
            criterion=self.criterion
        )

        if feat is None:

            leaf = leaf_value(y)

            if self.debug:
                print(">> Tidak ada split terbaik")
                print(f">> Leaf            : {leaf}")

            return leaf

        if self.debug:
            print(f"Feature Terbaik    : {feat}")
            print(f"Threshold          : {threshold}")
            print(f"Impurity           : {impurity:.4f}")

        left_X, left_y, right_X, right_y = split_data(
            X,
            y,
            feat,
            threshold
        )

        if self.debug:
            print(f"Left Sample        : {len(left_y)}")
            print(f"Right Sample       : {len(right_y)}")

        left_branch = self.build_tree(
            left_X,
            left_y,
            depth + 1
        )

        right_branch = self.build_tree(
            right_X,
            right_y,
            depth + 1
        )

        return {
            "feat": feat,
            "threshold": threshold,
            "left": left_branch,
            "right": right_branch
        }

    def _traverse(self, x, node):

        if not isinstance(node, dict):
            return node

        feat = node["feat"]
        threshold = node["threshold"]

        if x[feat] <= threshold:
            return self._traverse(x, node["left"])

        return self._traverse(x, node["right"])

    def predict(self, X):

        return np.array([
            self._traverse(x, self.tree)
            for x in X
        ])

class DecisionTree:

    def __init__(
        self,
        max_depth=5,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features='sqrt',
        criterion='gini',
        debug=False
    ):

        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.criterion = criterion
        self.debug = debug

        self.tree = None

    def fit(self, X, y):

        if self.debug:
            print("\n==============================")
            print("MEMULAI PEMBUATAN DECISION TREE")
            print("==============================")

        self.tree = self.build_tree(X, y)

    def build_tree(self, X, y, depth=0):

        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))

        if self.debug:
            print(f"\nDepth              : {depth}")
            print(f"Jumlah Sample      : {n_samples}")
            print(f"Jumlah Class       : {n_classes}")

        # kondisi stop
        if (
            depth >= self.max_depth or
            n_classes == 1 or
            n_samples < self.min_samples_split
        ):

            leaf = leaf_value(y)

            if self.debug:
                print(">> Membuat LEAF")
                print(f">> Nilai leaf      : {leaf}")

            return leaf

        feat, threshold, impurity = best_split(
            X,
            y,
            min_samples_leaf=self.min_samples_leaf,
            max_features=self.max_features,
            criterion=self.criterion
        )

        if feat is None:

            leaf = leaf_value(y)

            if self.debug:
                print(">> Tidak ada split terbaik")
                print(f">> Leaf            : {leaf}")

            return leaf

        if self.debug:
            print(f"Feature Terbaik    : {feat}")
            print(f"Threshold          : {threshold}")
            print(f"Impurity           : {impurity:.4f}")

        left_X, left_y, right_X, right_y = split_data(
            X,
            y,
            feat,
            threshold
        )

        if self.debug:
            print(f"Left Sample        : {len(left_y)}")
            print(f"Right Sample       : {len(right_y)}")

        left_branch = self.build_tree(
            left_X,
            left_y,
            depth + 1
        )

        right_branch = self.build_tree(
            right_X,
            right_y,
            depth + 1
        )

        return {
            "feat": feat,
            "threshold": threshold,
            "left": left_branch,
            "right": right_branch
        }

    def _traverse(self, x, node):

        if not isinstance(node, dict):
            return node

        feat = node["feat"]
        threshold = node["threshold"]

        if x[feat] <= threshold:
            return self._traverse(x, node["left"])

        return self._traverse(x, node["right"])

    def predict(self, X):

        return np.array([
            self._traverse(x, self.tree)
            for x in X
        ])
