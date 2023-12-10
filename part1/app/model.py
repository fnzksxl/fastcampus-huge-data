from sqlalchemy import Column, Integer, DateTime, func


# 테이블의 기본이 되는 인덱스, 생성시각, 변경시각을 사전 정의해두자
class BaseMin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
