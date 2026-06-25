from fastapi import APIRouter, Depends

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_db

router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "RLFlow API",
        "version": "0.1.0"
    }


@router.get("/db")
async def database_health_check(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    value = result.scalar()

    return {
        "status": "ok",
        "database": "connected",
        "result": value
    }
