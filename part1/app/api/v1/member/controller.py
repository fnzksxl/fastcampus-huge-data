from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api.v1.member.schema import memberRegister
from app.api.v1.member.service import memberSave
from app.database import get_db

router = APIRouter(tags=["Member"])


@router.post("")
async def insert(memberRegister: memberRegister, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. 회원정보(이메일, 닉네임, 생년월일)를 등록한다.
    2. 닉네임은 10자를 넘길 수 없다.
    ------------

    --- 파라미터 ---
    1. memberRegister
      - email : str
      - nikcname : str
      - birthday : datetime
    ---------------
    """
    return await memberSave(memberRegister, db)
