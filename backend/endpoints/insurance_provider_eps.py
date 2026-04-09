from fastapi import APIRouter, HTTPException
from schema.insurance_provider import InsuranceProviderModel, InsuranceProviderSchema


class InsuranceProviderEPS:
    def __init__(self, insurance_provider_dao):
        self.insurance_provider_dao = insurance_provider_dao
        self.router = APIRouter(prefix="/insurance-providers", tags=["Insurance Providers"])
        self.router.add_api_route("", self.get_all_insurance_providers, methods=["GET"])
        self.router.add_api_route("/{provider_id}", self.get_insurance_provider_by_id, methods=["GET"])
        self.router.add_api_route("", self.create_insurance_provider, methods=["POST"])
        self.router.add_api_route("/{provider_id}", self.update_insurance_provider, methods=["PUT"])
        self.router.add_api_route("/{provider_id}", self.delete_insurance_provider, methods=["DELETE"])

    def _to_dict(self, ip):
        return {"id": ip.ID, "name": ip.Name}

    async def get_all_insurance_providers(self):
        return [self._to_dict(ip) for ip in self.insurance_provider_dao.get_all_insurance_providers()]

    async def get_insurance_provider_by_id(self, provider_id: int):
        ip = self.insurance_provider_dao.get_insurance_provider_by_id(provider_id)
        if not ip:
            raise HTTPException(status_code=404, detail="Insurance provider not found")
        return self._to_dict(ip)

    async def create_insurance_provider(self, provider: InsuranceProviderModel):
        schema = InsuranceProviderSchema(Name=provider.name)
        return self._to_dict(self.insurance_provider_dao.create_insurance_provider(schema))

    async def update_insurance_provider(self, provider_id: int, provider: InsuranceProviderModel):
        existing = self.insurance_provider_dao.get_insurance_provider_by_id(provider_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Insurance provider not found")
        existing.Name = provider.name
        return self._to_dict(self.insurance_provider_dao.update_insurance_provider(existing))

    async def delete_insurance_provider(self, provider_id: int):
        if not self.insurance_provider_dao.delete_insurance_provider(provider_id):
            raise HTTPException(status_code=404, detail="Insurance provider not found")
        return {"deleted": provider_id}
