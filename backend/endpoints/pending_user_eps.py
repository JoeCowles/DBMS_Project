from fastapi import APIRouter, HTTPException
from schema.pending_user import PendingUserModel, PendingUserSchema


class PendingUserEPS:
    def __init__(self, pending_user_dao):
        self.pending_user_dao = pending_user_dao
        self.router = APIRouter(prefix="/pendingUsers", tags=["PendingUsers"])
        self.router.add_api_route("", self.get_all_pending_users, methods=["GET"])
        self.router.add_api_route("/{pending_id}", self.get_pending_user_by_id, methods=["GET"])
        self.router.add_api_route("", self.create_pending_user, methods=["POST"])
        self.router.add_api_route("/{pending_id}", self.update_pending_user, methods=["PUT"])
        self.router.add_api_route("/{pending_id}", self.delete_pending_user, methods=["DELETE"])

    def _to_dict(self, p):
        return {
            "id": p.Id,
            "firstName": p.FirstName,
            "lastName": p.LastName,
            "email": p.Email,
            "organization": p.Organization,
            "role": p.Role,
            "comment": p.Comment,
            "status": p.Status,
            "createdAt": p.CreatedAt.isoformat() if p.CreatedAt else None,
        }

    async def get_all_pending_users(self):
        return [self._to_dict(p) for p in self.pending_user_dao.get_all_pending_users()]

    async def get_pending_user_by_id(self, pending_id: int):
        pending = self.pending_user_dao.get_pending_user_by_id(pending_id)
        if not pending:
            raise HTTPException(status_code=404, detail="Pending user not found")
        return self._to_dict(pending)

    async def create_pending_user(self, pending_user: PendingUserModel):
        existing = self.pending_user_dao.get_pending_user_by_email(pending_user.email)
        if existing:
            raise HTTPException(
                status_code=409,
                detail="A pending request with this email already exists",
            )
        schema = PendingUserSchema(
            FirstName=pending_user.firstName,
            LastName=pending_user.lastName,
            Email=pending_user.email,
            Organization=pending_user.organization,
            Role=pending_user.role,
            Comment=pending_user.comment,
            Status="pending",
        )
        return self._to_dict(self.pending_user_dao.create_pending_user(schema))

    async def update_pending_user(self, pending_id: int, pending_user: PendingUserModel):
        existing = self.pending_user_dao.get_pending_user_by_id(pending_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Pending user not found")
        existing.FirstName = pending_user.firstName
        existing.LastName = pending_user.lastName
        existing.Email = pending_user.email
        existing.Organization = pending_user.organization
        existing.Role = pending_user.role
        existing.Comment = pending_user.comment
        return self._to_dict(self.pending_user_dao.update_pending_user(existing))

    async def delete_pending_user(self, pending_id: int):
        if not self.pending_user_dao.delete_pending_user(pending_id):
            raise HTTPException(status_code=404, detail="Pending user not found")
        return {"deleted": pending_id}
