import numpy as np
from app.ml.utils.loader import get_model
from app.ml.services.preprocess import transform_input

model = get_model()

def predict(data):

    X = transform_input(data)

    # print(X)
    # print(type(X))
    # print(X.shape)

    # result = model.predict(X)

    # return int(result[0])
    prediction = model.predict(X)[0]

    probabilities = model.predict_proba(X)[0]

    return {
        "prediction": int(prediction),

        "label":
            "ASD Detected"
            if prediction == 1
            else "No ASD Detected",

        "probability": {
            "no_asd": round(float(probabilities[0]) * 100, 2),
            "asd": round(float(probabilities[1]) * 100, 2)
    }
}