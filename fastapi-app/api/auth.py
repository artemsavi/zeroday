import bcrypt
import jwt

from fastapi import Form, HTTPException, status
from jwt import InvalidTokenError
from datetime import datetime, timedelta, UTC

from .config import settings
from .users_log_pass_db import users_db


# encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
# jwt.decode(encoded, public_key, algorithms=["RS256"])


def compare_passwords(pwd: str, hashed_pwd: bytes):
    return bcrypt.checkpw(pwd.encode(), hashed_pwd)


def validate_user(
    username: str = Form(),
    password: str = Form(),
):
    user = users_db.get(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"user not found, try again",
        )
    if not compare_passwords(password, user.get("hashed_password")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="wrong password...",
        )
    return user


def create_access_token(user: dict):
    expires = datetime.now(UTC) + timedelta(minutes=settings.expires_in_minutes)
    jwt_payload = {
        "sub": user["username"],
        "exp": expires,
    }
    token = jwt.encode(jwt_payload, settings.private_key, algorithm=settings.algorithm)
    return token


def get_current_user(token):
    try:
        payload = jwt.decode(
            jwt=token,
            key=settings.public_key,
            algorithms=settings.algorithm,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="wrong access key, try again",
        )
    user = users_db.get(payload["sub"])

    return user
