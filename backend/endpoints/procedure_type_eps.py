from fastapi import APIRouter, HTTPException
from schema.procedure_type import ProcedureTypeModel, ProcedureTypeSchema


class ProcedureTypeEPS:
    def __init__(self, procedure_type_dao):
        self.procedure_type_dao = procedure_type_dao
        self.router = APIRouter(prefix="/procedure-types", tags=["Procedure Types"])
        self.router.add_api_route("", self.get_all_procedure_types, methods=["GET"])
        self.router.add_api_route("/{procedure_type_id}", self.get_procedure_type_by_id, methods=["GET"])
        self.router.add_api_route("", self.create_procedure_type, methods=["POST"])
        self.router.add_api_route("/{procedure_type_id}", self.update_procedure_type, methods=["PUT"])
        self.router.add_api_route("/{procedure_type_id}", self.delete_procedure_type, methods=["DELETE"])

    def _to_dict(self, pt):
        return {"id": pt.ID, "name": pt.Name, "description": pt.Description}

    async def get_all_procedure_types(self):
        return [self._to_dict(pt) for pt in self.procedure_type_dao.get_all_procedure_types()]

    async def get_procedure_type_by_id(self, procedure_type_id: int):
        pt = self.procedure_type_dao.get_procedure_type_by_id(procedure_type_id)
        if not pt:
            raise HTTPException(status_code=404, detail="Procedure type not found")
        return self._to_dict(pt)

    async def create_procedure_type(self, procedure_type: ProcedureTypeModel):
        schema = ProcedureTypeSchema(Name=procedure_type.name, Description=procedure_type.description)
        return self._to_dict(self.procedure_type_dao.create_procedure_type(schema))

    async def update_procedure_type(self, procedure_type_id: int, procedure_type: ProcedureTypeModel):
        existing = self.procedure_type_dao.get_procedure_type_by_id(procedure_type_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Procedure type not found")
        existing.Name = procedure_type.name
        existing.Description = procedure_type.description
        return self._to_dict(self.procedure_type_dao.update_procedure_type(existing))

    async def delete_procedure_type(self, procedure_type_id: int):
        if not self.procedure_type_dao.delete_procedure_type(procedure_type_id):
            raise HTTPException(status_code=404, detail="Procedure type not found")
        return {"deleted": procedure_type_id}
