from fastapi import APIRouter
from app.api.v1.member import controller as memberCtrl
from app.api.v1.follow import controller as followCtrl

router = APIRouter()
router.include_router(memberCtrl.router, prefix="/member")
router.include_router(followCtrl.router, prefix="/follow")
