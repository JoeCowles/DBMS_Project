from fastapi import APIRouter, HTTPException
from schema.procedure import ProcedureModel, ProcedureSchema


class ProcedureEPS:
    def __init__(self, procedure_dao):
        self.procedure_dao = procedure_dao
        self.router = APIRouter(prefix="/procedures", tags=["Procedures"])
        self.router.add_api_route("", self.get_all_procedures, methods=["GET"])
        self.router.add_api_route("/{procedure_id}", self.get_procedure_by_id, methods=["GET"])
        self.router.add_api_route("", self.create_procedure, methods=["POST"])
        self.router.add_api_route("/{procedure_id}", self.update_procedure, methods=["PUT"])
        self.router.add_api_route("/{procedure_id}", self.delete_procedure, methods=["DELETE"])

    def _to_dict(self, p):
        return {
            "id": p.ID,
            "procedure_type_id": p.ProcedureTypeID,
            "user_id": p.UserID,
            "date_of_service": str(p.DateOfService),
        }

    async def get_all_procedures(self):
        return [self._to_dict(p) for p in self.procedure_dao.get_all_procedures()]

    async def get_procedure_by_id(self, procedure_id: int):
        p = self.procedure_dao.get_procedure_by_id(procedure_id)
        if not p:
            raise HTTPException(status_code=404, detail="Procedure not found")
        return self._to_dict(p)

    async def create_procedure(self, procedure: ProcedureModel):
        schema = ProcedureSchema(
            ProcedureTypeID=procedure.procedure_type_id,
            UserID=procedure.user_id,
            DateOfService=procedure.date_of_service,
        )
        return self._to_dict(self.procedure_dao.create_procedure(schema))

    async def update_procedure(self, procedure_id: int, procedure: ProcedureModel):
        existing = self.procedure_dao.get_procedure_by_id(procedure_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Procedure not found")
        existing.ProcedureTypeID = procedure.procedure_type_id
        existing.UserID = procedure.user_id
        existing.DateOfService = procedure.date_of_service
        return self._to_dict(self.procedure_dao.update_procedure(existing))

    async def delete_procedure(self, procedure_id: int):
        if not self.procedure_dao.delete_procedure(procedure_id):
            raise HTTPException(status_code=404, detail="Procedure not found")
        return {"deleted": procedure_id}
