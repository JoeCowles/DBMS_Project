from pydantic import BaseModel
from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint, func
from .base import Base

class UserFavoriteModel(BaseModel):
    user_id: int
    policy_coverage_id: int

    class Config:
        from_attributes = True

class UserFavoriteSchema(Base):
    __tablename__ = "UserFavorite"
    __table_args__ = (
        UniqueConstraint("UserID", "PolicyCoverageID", name="uq_user_favorite"),
    )

    ID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey("Users.ID", ondelete="CASCADE"), nullable=False)
    PolicyCoverageID = Column(Integer, ForeignKey("PolicyCoverage.ID", ondelete="CASCADE"), nullable=False)
    AddedAt = Column(DateTime, server_default=func.now(), nullable=False)
