from fastapi import APIRouter

from app.ml.registry.questions import QUESTIONS


router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


@router.get("/")
def get_questions():

    results = []

    for field, meta in QUESTIONS.items():

        item = {
            "field": field,
            "question": meta["question"],
            "type": meta["type"]
        }

        # optional choices
        if "choices" in meta:
            item["choices"] = meta["choices"]

        results.append(item)

    return {
        "total": len(results),
        "questions": results
    }