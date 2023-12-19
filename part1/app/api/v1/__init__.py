from fastapi import APIRouter
from app.api.v1.member import controller as memberCtrl
from app.api.v1.follow import controller as followCtrl
from app.api.v1.post import controller as postCtrl

router = APIRouter()
router.include_router(memberCtrl.router, prefix="/member")
router.include_router(followCtrl.router, prefix="/follow")
router.include_router(postCtrl.router, prefix="/post")
