import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from schema.base import Base

from daos.user_dao import UserDAO
from daos.procedure_type_dao import ProcedureTypeDAO
from daos.procedure_dao import ProcedureDAO
from daos.insurance_provider_dao import InsuranceProviderDAO
from daos.policy_dao import PolicyDAO
from daos.policy_coverage_dao import PolicyCoverageDAO

from endpoints import (
    UserEPS,
    ProcedureTypeEPS,
    ProcedureEPS,
    InsuranceProviderEPS,
    PolicyEPS,
    PolicyCoverageEPS,
)


import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:////app/db/database.db")
print(f"[DB] Connecting to: {DATABASE_URL}")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import all schema models so their tables are registered on Base.metadata
import schema  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI()

db = SessionLocal()
user_dao = UserDAO(db)
procedure_type_dao = ProcedureTypeDAO(db)
procedure_dao = ProcedureDAO(db)
insurance_provider_dao = InsuranceProviderDAO(db)
policy_dao = PolicyDAO(db)
policy_coverage_dao = PolicyCoverageDAO(db)

# Endpoints
user_eps = UserEPS(user_dao)
procedure_type_eps = ProcedureTypeEPS(procedure_type_dao)
procedure_eps = ProcedureEPS(procedure_dao)
insurance_provider_eps = InsuranceProviderEPS(insurance_provider_dao)
policy_eps = PolicyEPS(policy_dao)
policy_coverage_eps = PolicyCoverageEPS(policy_coverage_dao)

# Register routers
app.include_router(user_eps.router)
app.include_router(procedure_type_eps.router)
app.include_router(procedure_eps.router)
app.include_router(insurance_provider_eps.router)
app.include_router(policy_eps.router)
app.include_router(policy_coverage_eps.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
