from pydantic import BaseModel, Field
from datetime import datetime


class AnalyzeRequest(BaseModel):
    text: str = Field(..., max_length=1000, description="Исходный текст для анализа")


class AnalyzeResponse(BaseModel):
    metrics: dict[str, float] = Field(..., description="Рассчитанные метрики текста")


class AdaptRequest(BaseModel):
    text: str = Field(..., max_length=1000)
    target_style: str = Field(..., description="Целевой стиль адаптации")


class AdaptResponse(BaseModel):
    adapted_text: str
    target_style: str
    confidence: float = Field(ge=0.0, le=1.0)


class StyleSchema(BaseModel):
    id: int
    name: str
    description: str | None = None


class HistoryItem(BaseModel):
    id: int
    original_text: str
    adapted_text: str | None = None
    target_style: str | None = None
    created_at: datetime


class HistoryResponse(BaseModel):
    items: list[HistoryItem]
