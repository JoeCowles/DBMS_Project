from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from .base import Base

class UserPreferenceModel(BaseModel):
    user_id: int
    preference: str

    class Config:
        from_attributes = True

class UserPreferenceSchema(Base):
    __tablename__ = "UserPreference"
    __table_args__ = (
        UniqueConstraint("UserID", name="uq_user_preference_user"),
    )

    ID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey("Users.ID", ondelete="CASCADE"), nullable=False)
    Preference = Column(String, nullable=False)
