from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class PolicyModel(BaseModel):
    id: int | None = None
    insurance_provider_id: int
    name: str
    deductible: str

    class Config:
        from_attributes = True


class PolicySchema(Base):
    __tablename__ = "Policy"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    InsuranceProviderID = Column(Integer, ForeignKey("InsuranceProvider.ID", ondelete="CASCADE"), nullable=False)
    Name = Column(String, nullable=False)
    Deductible = Column(String, nullable=False)
