from .adapt import router as adapt_router
from .analyze import router as analyze_router
from .health import router as health_router
from .history import router as history_router
from .styles import router as styles_router

__all__ = [
    "adapt_router",
    "analyze_router",
    "health_router",
    "history_router",
    "styles_router",
]
