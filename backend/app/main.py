from fastapi import FastAPI
from app.routes.model_routes import router as model_router
from app.routes.question_routes import router as question_router

app = FastAPI(
    title="API Skripsi Random Forest",
    version="0.1.0",
    description="API untuk klasifikasi Random Forest menggunakan FastAPI"
)
@app.get("/",tags=["General"])
def read_root():
    return {"Hello": "World"}

app.include_router(model_router)
app.include_router(question_router)