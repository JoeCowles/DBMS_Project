from pydantic import BaseModel
from sqlalchemy import Column, String
from .base import Base


class UserModel(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserSchema(Base):
    __tablename__ = "Users"

    Username = Column(String, primary_key=True)
    Email = Column(String, nullable=False)
    Password = Column(String, nullable=False)
