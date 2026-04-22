from typing import Optional
from fastapi import APIRouter, HTTPException
from schema.policy_coverage import PolicyCoverageModel, PolicyCoverageSchema


class PolicyCoverageEPS:
    def __init__(self, policy_coverage_dao):
        self.policy_coverage_dao = policy_coverage_dao
        self.router = APIRouter(prefix="/policy-coverages", tags=["Policy Coverages"])
        self.router.add_api_route("/search", self.search_policy_coverages, methods=["GET"])
        self.router.add_api_route("", self.get_all_policy_coverages, methods=["GET"])
        self.router.add_api_route("/{coverage_id}/details", self.get_coverage_details, methods=["GET"])
        self.router.add_api_route("/{coverage_id}", self.get_policy_coverage_by_id, methods=["GET"])
        self.router.add_api_route("", self.create_policy_coverage, methods=["POST"])
        self.router.add_api_route("/{coverage_id}", self.update_policy_coverage, methods=["PUT"])
        self.router.add_api_route("/{coverage_id}", self.delete_policy_coverage, methods=["DELETE"])

    def _to_dict(self, c):
        return {
            "id": c.ID,
            "policy_id": c.PolicyID,
            "procedure_type_id": c.ProcedureTypeID,
            "description": c.Description,
            "link_to_original": c.LinkToOriginal,
            "start_date": str(c.StartDate),
            "end_date": str(c.EndDate),
        }

    async def search_policy_coverages(
        self,
        name: Optional[str] = None,
        cpt_code: Optional[str] = None,
        provider: Optional[str] = None,
        procedure_type_id: Optional[int] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        latest_only: bool = False,
    ):
        rows = self.policy_coverage_dao.search(
            name=name,
            cpt_code=cpt_code,
            provider=provider,
            procedure_type_id=procedure_type_id,
            date_from=date_from,
            date_to=date_to,
            latest_only=latest_only,
        )
        return [dict(r) for r in rows]

    async def get_coverage_details(self, coverage_id: int):
        details = self.policy_coverage_dao.get_coverage_details(coverage_id)
        if not details:
            raise HTTPException(status_code=404, detail="Policy coverage not found")
        return details

    async def get_all_policy_coverages(self):
        return [self._to_dict(c) for c in self.policy_coverage_dao.get_all_policy_coverages()]

    async def get_policy_coverage_by_id(self, coverage_id: int):
        coverage = self.policy_coverage_dao.get_policy_coverage_by_id(coverage_id)
        if not coverage:
            raise HTTPException(status_code=404, detail="Policy coverage not found")
        return self._to_dict(coverage)

    async def create_policy_coverage(self, coverage: PolicyCoverageModel):
        schema = PolicyCoverageSchema(
            PolicyID=coverage.policy_id,
            ProcedureTypeID=coverage.procedure_type_id,
            Description=coverage.description,
            LinkToOriginal=coverage.link_to_original,
            StartDate=coverage.start_date,
            EndDate=coverage.end_date,
        )
        return self._to_dict(self.policy_coverage_dao.create_policy_coverage(schema))

    async def update_policy_coverage(self, coverage_id: int, coverage: PolicyCoverageModel):
        existing = self.policy_coverage_dao.get_policy_coverage_by_id(coverage_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Policy coverage not found")
        existing.PolicyID = coverage.policy_id
        existing.ProcedureTypeID = coverage.procedure_type_id
        existing.Description = coverage.description
        existing.LinkToOriginal = coverage.link_to_original
        existing.StartDate = coverage.start_date
        existing.EndDate = coverage.end_date
        return self._to_dict(self.policy_coverage_dao.update_policy_coverage(existing))

    async def delete_policy_coverage(self, coverage_id: int):
        if not self.policy_coverage_dao.delete_policy_coverage(coverage_id):
            raise HTTPException(status_code=404, detail="Policy coverage not found")
        return {"deleted": coverage_id}
