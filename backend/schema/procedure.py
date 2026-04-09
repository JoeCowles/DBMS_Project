from pydantic import BaseModel
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .base import Base


class ProcedureModel(BaseModel):
    id: int | None = None
    procedure_type_id: int
    user_id: str
    date_of_service: date

    class Config:
        from_attributes = True


class ProcedureSchema(Base):
    __tablename__ = "Procedure"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ProcedureTypeID = Column(Integer, ForeignKey("ProcedureType.ID", ondelete="CASCADE"), nullable=False)
    UserID = Column(String, ForeignKey("Users.Username", ondelete="CASCADE"), nullable=False)
    DateOfService = Column(Date, nullable=False)
