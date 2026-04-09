from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .base import Base


class ProcedureTypeModel(BaseModel):
    id: int | None = None
    name: str
    description: str

    class Config:
        from_attributes = True


class ProcedureTypeSchema(Base):
    __tablename__ = "ProcedureType"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
