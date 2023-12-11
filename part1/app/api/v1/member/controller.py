from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm.session import Session

from app.api.v1.member.schema import memberRegister, memberFind, memberUpdate
from app.api.v1.member.service import memberSave, memberSearch, memberUpdateNickname
from app.database import get_db

router = APIRouter(tags=["Member"])


@router.post("", status_code=201)
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


@router.get("/{id}", response_model=memberFind, status_code=200)
async def find(id: int = Path(...), db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. 회원의 Index(Id)를 이용해서 회원 정보를 반환한다.
    ------------
    --- Path 파라미터 ---
    1. id: int
    ---------------
    """
    return await memberSearch(id, db)


@router.put("/{id}", response_model=memberFind, status_code=202)
async def updateNickname(id: int = Path(...), newName=memberUpdate, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. 회원의 Index(Id)를 이용해 Nickname을 수정한다
    ------------
    --- Path 파라미터 ---
    1. id: int
    --------------------
    """
    return await memberUpdateNickname(id, newName, db)
