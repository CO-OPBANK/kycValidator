from fastapi import APIRouter

from models import create_session
from models import do_liveness_check

router = APIRouter(
    prefix="/liveness",
    tags=["livenessCheck"],
)


@router.get("/session")
async def get_create_session():
    return create_session()


@router.get("/check/{session_id}")
async def check_liveness(session_id):
    return do_liveness_check(session_id)
