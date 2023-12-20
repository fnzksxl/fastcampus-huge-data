from sqlalchemy import Column, Integer, DateTime, func, String, Index
from sqlalchemy.sql.schema import ForeignKey


from app.database import Base


# 테이블의 기본이 되는 인덱스, 생성시각, 변경시각을 사전 정의해두자
class BaseMin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class Member(Base, BaseMin):
    __tablename__ = "member"

    email = Column(String(25), nullable=False, unique=True)
    nickname = Column(String(10), nullable=False)
    birthday = Column(DateTime, nullable=False)

    # Member 객체를 Dictionary 형태로 변환할 수 있음
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Follow(Base, BaseMin):
    __tablename__ = "follow"

    fromMemberId = Column(Integer, ForeignKey("member.id"))
    toMemberId = Column(Integer, ForeignKey("member.id"))

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Post(Base, BaseMin):
    __tablename__ = "post"

    memberId = Column(Integer, ForeignKey("member.id"))
    content = Column(String(255))

    __table_args__ = (Index("idx_post_created_member", "created_at", "memberId"),)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# 과거의 기록을 가지고 있는 History => 정규화의 대상 X
# (데이터가 항상 최신성을 요구하는지? = 과거의 기록을 남겨야 하는지?)
class MemberNicknameHistory(Base, BaseMin):
    __tablename__ = "member_nickname_history"

    nickname = Column(String(10), nullable=False)
    memberId = Column(Integer, ForeignKey("member.id"))

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Timeline(Base, BaseMin):
    __tablename__ = "timeline"

    memberId = Column(Integer, ForeignKey("member.id"))
    postId = Column(Integer, ForeignKey("post.id"))

    __table_args__ = (Index("idx_member_post_id", "postId", "memberId"),)
