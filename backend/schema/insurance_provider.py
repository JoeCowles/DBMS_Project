from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .base import Base


class InsuranceProviderModel(BaseModel):
    id: int | None = None
    name: str

    class Config:
        from_attributes = True


class InsuranceProviderSchema(Base):
    __tablename__ = "InsuranceProvider"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
