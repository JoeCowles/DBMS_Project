from fastapi import APIRouter

class PolicyEPS:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/policies", self.get_policies, methods=["GET"])

    async def get_policies(self):
        return {"message": "Policies"}