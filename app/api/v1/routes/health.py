from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "RLFlow API",
        "version": "0.1.0"
    }
