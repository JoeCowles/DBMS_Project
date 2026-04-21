from pydantic import BaseModel
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, func
from .base import Base


class PolicyCoverageModel(BaseModel):
    id: int | None = None
    policy_id: int
    procedure_type_id: int
    description: str
    link_to_original: str
    start_date: date
    end_date: date
    document_url: str | None = None
    added_date: datetime | None = None

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
    DocumentURL = Column(String, nullable=True)
    AddedDate = Column(DateTime, server_default=func.now(), nullable=True)
