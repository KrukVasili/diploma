from fastapi import APIRouter
from app.models.schemas import StyleSchema

router = APIRouter()


@router.get("/styles", response_model=list[StyleSchema], tags=["styles"])
async def get_styles():
    return [
        {
            "id": 1,
            "name": "Официально-деловой",
            "description": "Стандартизированная лексика, отсутствие эмоциональной окраски",
        },
        {
            "id": 2,
            "name": "Научно-академический",
            "description": "Терминологически насыщенный, чёткая логическая структура",
        },
        {
            "id": 3,
            "name": "Профессиональный жаргон",
            "description": "Специализированная лексика, допускает сокращения",
        },
        {
            "id": 4,
            "name": "Разговорно-бытовой",
            "description": "Нейтральная повседневная речь",
        },
        {
            "id": 5,
            "name": "Молодёжный сленг",
            "description": "Высокая динамичность, заимствования, эмоциональная экспрессия",
        },
    ]
