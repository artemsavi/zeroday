from pathlib import Path
from typing import ClassVar

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    private_key: ClassVar[str] = Path("certs/rs256_private.pem").read_text()
    public_key: ClassVar[str] = Path("certs/rs256_public.pem").read_text()
    algorithm: str = "RS256"
    expires_in_minutes: int = 15


settings = Settings()
