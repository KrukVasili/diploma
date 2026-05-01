import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.api import (
    adapt_router,
    analyze_router,
    health_router,
    history_router,
    styles_router,
)

setup_logging(debug=settings.DEBUG)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url=f"{settings.API_PREFIX}/docs",
    redoc_url=f"{settings.API_PREFIX}/redoc",
    lifespan=lifespan,
)

app.include_router(health_router, prefix=settings.API_PREFIX, tags=["health"])
app.include_router(analyze_router, prefix=settings.API_PREFIX)
app.include_router(adapt_router, prefix=settings.API_PREFIX)
app.include_router(styles_router, prefix=settings.API_PREFIX)
app.include_router(history_router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)
