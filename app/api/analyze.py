from fastapi import APIRouter
from app.models.schemas import AnalyzeRequest, AnalyzeResponse

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse, tags=["analyze"])
async def analyze_text(request: AnalyzeRequest):
    words = request.text.split()
    return {
        "metrics": {
            "word_count": len(words),
            "sentence_count": sum(1 for c in request.text if c in ".!?"),
            "avg_word_length": sum(len(w) for w in words) / max(len(words), 1),
        }
    }
