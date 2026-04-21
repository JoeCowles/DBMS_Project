from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String, Text

from .base import Base


class PendingUserModel(BaseModel):
    firstName: str
    lastName: str
    email: str
    organization: str
    role: str
    comment: Optional[str] = None

    class Config:
        from_attributes = True


class PendingUserSchema(Base):
    __tablename__ = "PendingUsers"

    Id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Organization = Column(String, nullable=False)
    Role = Column(String, nullable=False)
    Comment = Column(Text, nullable=True)
    Status = Column(String, nullable=False, default="pending")
    CreatedAt = Column(DateTime, nullable=False, default=datetime.utcnow)
