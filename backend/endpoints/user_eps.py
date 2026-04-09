from fastapi import APIRouter, HTTPException
from schema.user import UserModel, UserSchema


class UserEPS:
    def __init__(self, user_dao):
        self.user_dao = user_dao
        self.router = APIRouter(prefix="/users", tags=["Users"])
        self.router.add_api_route("", self.get_all_users, methods=["GET"])
        self.router.add_api_route("/{username}", self.get_user_by_username, methods=["GET"])
        self.router.add_api_route("", self.create_user, methods=["POST"])
        self.router.add_api_route("/{username}", self.update_user, methods=["PUT"])
        self.router.add_api_route("/{username}", self.delete_user, methods=["DELETE"])

    def _to_dict(self, u):
        return {"username": u.Username, "email": u.Email, "password": u.Password}

    async def get_all_users(self):
        return [self._to_dict(u) for u in self.user_dao.get_all_users()]

    async def get_user_by_username(self, username: str):
        user = self.user_dao.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self._to_dict(user)

    async def create_user(self, user: UserModel):
        schema = UserSchema(Username=user.username, Email=user.email, Password=user.password)
        return self._to_dict(self.user_dao.create_user(schema))

    async def update_user(self, username: str, user: UserModel):
        existing = self.user_dao.get_user_by_username(username)
        if not existing:
            raise HTTPException(status_code=404, detail="User not found")
        existing.Email = user.email
        existing.Password = user.password
        return self._to_dict(self.user_dao.update_user(existing))

    async def delete_user(self, username: str):
        if not self.user_dao.delete_user(username):
            raise HTTPException(status_code=404, detail="User not found")
        return {"deleted": username}
