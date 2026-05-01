from fastapi import APIRouter
from app.models.schemas import AdaptRequest, AdaptResponse

router = APIRouter()


@router.post("/adapt", response_model=AdaptResponse, tags=["adapt"])
async def adapt_text(request: AdaptRequest):
    return {
        "adapted_text": f"[Адаптировано в стиль '{request.target_style}'] {request.text}",
        "target_style": request.target_style,
        "confidence": 0.85,
    }
