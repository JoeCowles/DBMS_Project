from fastapi import APIRouter
from schema.user_preference import UserPreferenceModel

class UserPreferenceEPS:
    def __init__(self, user_preference_dao):
        self.user_preference_dao = user_preference_dao
        self.router = APIRouter(prefix="/preferences", tags=["Preferences"])
        self.router.add_api_route("/{user_id}", self.get_preference, methods=["GET"])
        self.router.add_api_route("", self.set_preference, methods=["PUT"])

    def _to_dict(self, p):
        return {"id": p.ID, "user_id": p.UserID, "preference": p.Preference}

    async def get_preference(self, user_id: int):
        pref = self.user_preference_dao.get_for_user(user_id)
        if not pref:
            return {"user_id": user_id, "preference": None}
        return self._to_dict(pref)

    async def set_preference(self, body: UserPreferenceModel):
        pref = self.user_preference_dao.set_for_user(body.user_id, body.preference)
        return self._to_dict(pref)
