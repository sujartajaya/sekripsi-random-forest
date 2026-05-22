from fastapi import APIRouter
from app.ml.utils.loader import get_model_info
from app.schemas.predict_request import PredictRequest
from app.ml.services.predictor import predict

router = APIRouter(
    prefix="/model",
    tags=["Model"]
)


@router.get("/load-model")
def load_model():

    info = get_model_info()

    return {
        "status": "success",
        "message": "Model loaded successfully",
        "model_info": info
    }


@router.post("/predict")
def predict_route(request: PredictRequest):

    data = request.model_dump()

    result = predict(data)

    return {
        "prediction": result
    }