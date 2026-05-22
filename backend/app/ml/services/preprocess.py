import numpy as np

from app.ml.registry.features import FEATURE_ORDER
from app.ml.registry.mappings import MAPPINGS


def transform_input(data: dict):

    processed = {}

    for feature in FEATURE_ORDER:

        value = data[feature]

        # categorical mapping
        if feature in MAPPINGS:
            value = MAPPINGS[feature][value]

        # bool -> int
        elif isinstance(value, bool):
            value = int(value)

        processed[feature] = value

    ordered = [processed[f] for f in FEATURE_ORDER]

    return np.array([ordered])