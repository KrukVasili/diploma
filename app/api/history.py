from fastapi import APIRouter
from datetime import datetime
from app.models.schemas import HistoryResponse, HistoryItem

router = APIRouter()


@router.get("/history", response_model=HistoryResponse, tags=["history"])
async def get_history():
    return {
        "items": [
            {
                "id": 1,
                "original_text": "Пример исходного текста для истории",
                "adapted_text": "Пример адаптированного текста",
                "target_style": "Молодёжный сленг",
                "created_at": datetime.now(),
            }
        ]
    }
