from pydantic import BaseModel
from datetime import date
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .base import Base


class PolicyCoverageModel(BaseModel):
    id: int | None = None
    policy_id: int
    procedure_type_id: int
    description: str
    link_to_original: str
    start_date: date
    end_date: date

    class Config:
        from_attributes = True


class PolicyCoverageSchema(Base):
    __tablename__ = "PolicyCoverage"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PolicyID = Column(Integer, ForeignKey("Policy.ID", ondelete="CASCADE"), nullable=False)
    ProcedureTypeID = Column(Integer, ForeignKey("ProcedureType.ID", ondelete="CASCADE"), nullable=False)
    Description = Column(String, nullable=False)
    LinkToOriginal = Column(String, nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
