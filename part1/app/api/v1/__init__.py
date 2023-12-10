from fastapi import APIRouter
from app.api.v1.member import controller as memberCtrl

router = APIRouter()
router.include_router(memberCtrl.router, prefix="/v1/member")
