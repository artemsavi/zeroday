from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class AccessToken(BaseModel):
    token: str
    token_type: str = "Bearier"
