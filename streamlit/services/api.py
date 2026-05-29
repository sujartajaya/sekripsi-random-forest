import requests

API_URL = "http://fastapi:8000"

# =========================================
# GET QUESTIONS
# =========================================

def get_questions():

    response = requests.get(
        f"{API_URL}/questions",
        timeout=30
    )

    response.raise_for_status()

    return response.json()

# =========================================
# PREDICT
# =========================================

def predict(data):

    response = requests.post(
        f"{API_URL}/model/predict",
        json=data,
        timeout=30
    )

    response.raise_for_status()

    return response.json()

# =========================================
# GET MODEL INFO
# =========================================
def get_model_info():

    response = requests.get(
        f"{API_URL}/model/load-model",
        timeout=30
    )

    response.raise_for_status()

    return response.json() 