import uvicorn
from fastapi import FastAPI
from endpoints import PolicyEPS


class Main():
    app = FastAPI()

    policy_eps = PolicyEPS()
    app.include_router(policy_eps.router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}
        

if __name__ == "__main__":
    uvicorn.run("main:Main.app", host="0.0.0.0", port=8000, reload=True)
