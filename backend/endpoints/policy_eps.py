from fastapi import APIRouter, HTTPException
from schema.policy import PolicyModel, PolicySchema


class PolicyEPS:
    def __init__(self, policy_dao):
        self.policy_dao = policy_dao
        self.router = APIRouter(prefix="/policies", tags=["Policies"])
        self.router.add_api_route("", self.get_all_policies, methods=["GET"])
        self.router.add_api_route("/{policy_id}", self.get_policy_by_id, methods=["GET"])
        self.router.add_api_route("", self.create_policy, methods=["POST"])
        self.router.add_api_route("/{policy_id}", self.update_policy, methods=["PUT"])
        self.router.add_api_route("/{policy_id}", self.delete_policy, methods=["DELETE"])

    def _to_dict(self, p):
        return {
            "id": p.ID,
            "insurance_provider_id": p.InsuranceProviderID,
            "name": p.Name,
            "deductible": p.Deductible,
        }

    async def get_all_policies(self):
        return [self._to_dict(p) for p in self.policy_dao.get_all_policies()]

    async def get_policy_by_id(self, policy_id: int):
        policy = self.policy_dao.get_policy_by_id(policy_id)
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")
        return self._to_dict(policy)

    async def create_policy(self, policy: PolicyModel):
        schema = PolicySchema(
            InsuranceProviderID=policy.insurance_provider_id,
            Name=policy.name,
            Deductible=policy.deductible,
        )
        return self._to_dict(self.policy_dao.create_policy(schema))

    async def update_policy(self, policy_id: int, policy: PolicyModel):
        existing = self.policy_dao.get_policy_by_id(policy_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Policy not found")
        existing.InsuranceProviderID = policy.insurance_provider_id
        existing.Name = policy.name
        existing.Deductible = policy.deductible
        return self._to_dict(self.policy_dao.update_policy(existing))

    async def delete_policy(self, policy_id: int):
        if not self.policy_dao.delete_policy(policy_id):
            raise HTTPException(status_code=404, detail="Policy not found")
        return {"deleted": policy_id}