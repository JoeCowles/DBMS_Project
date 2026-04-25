from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .base import Base

class UserModel(BaseModel):
    id: int | None = None
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True

class UserSchema(Base):
    __tablename__ = "Users"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String, nullable=False, unique=True)
    Email = Column(String, nullable=False)
    Password = Column(String, nullable=False)
