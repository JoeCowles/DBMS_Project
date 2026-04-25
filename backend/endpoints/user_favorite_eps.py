from fastapi import APIRouter, HTTPException
from schema.user_favorite import UserFavoriteModel

class UserFavoriteEPS:
    def __init__(self, user_favorite_dao):
        self.user_favorite_dao = user_favorite_dao
        self.router = APIRouter(prefix="/favorites", tags=["Favorites"])
        self.router.add_api_route("", self.list_favorites, methods=["GET"])
        self.router.add_api_route("/ids", self.list_favorite_ids, methods=["GET"])
        self.router.add_api_route("", self.add_favorite, methods=["POST"])
        self.router.add_api_route(
            "/{user_id}/{policy_coverage_id}", self.remove_favorite, methods=["DELETE"]
        )

    async def list_favorites(self, user_id: int):
        rows = self.user_favorite_dao.list_for_user(user_id)
        return [dict(r) for r in rows]

    async def list_favorite_ids(self, user_id: int):
        return self.user_favorite_dao.ids_for_user(user_id)

    async def add_favorite(self, favorite: UserFavoriteModel):
        fav = self.user_favorite_dao.add(favorite.user_id, favorite.policy_coverage_id)
        if fav is None:
            return {"user_id": favorite.user_id, "policy_coverage_id": favorite.policy_coverage_id, "already_favorited": True}
        return {"user_id": fav.UserID, "policy_coverage_id": fav.PolicyCoverageID}

    async def remove_favorite(self, user_id: int, policy_coverage_id: int):
        if not self.user_favorite_dao.remove(user_id, policy_coverage_id):
            raise HTTPException(status_code=404, detail="Favorite not found")
        return {"deleted": True}
