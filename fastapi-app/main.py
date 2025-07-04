import uvicorn
from fastapi import FastAPI, Depends

from api.auth import validate_user, create_access_token, get_current_user

app = FastAPI()


@app.post("/login")
def auth_user_issue_token(user=Depends(validate_user)):
    token = create_access_token(user)
    return {"token": token}


@app.get("/check")
def check_user_info(user=Depends(get_current_user)):
    return {
        "name": user["username"],
        "salary": user["salary"],
        "next_raise_at": user["next_raise_at"],
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
