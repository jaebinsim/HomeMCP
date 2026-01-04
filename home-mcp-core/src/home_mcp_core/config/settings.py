from __future__ import annotations

from pathlib import Path
from typing import Any
import tomllib
from pydantic import BaseModel, AnyHttpUrl, Field


BASE_DIR = Path(__file__).resolve().parent


class TuyaSettings(BaseModel):
    access_id: str = Field(alias="access_id")
    access_key: str = Field(alias="access_key")
    username: str
    password: str
    endpoint: str = "https://openapi.tuya.com"
    country_code: str = Field(default="82")
    app_schema: str = Field(default="tuyaSmart", alias="schema")


class WindowsAgentSettings(BaseModel):
    base_url: AnyHttpUrl


class Settings(BaseModel):
    tuya: TuyaSettings
    windows_agent: WindowsAgentSettings


def load_settings(path: Path | str | None = None) -> Settings:
    if path is None:
        path = BASE_DIR / "settings.toml"

    path = Path(path)
    data: dict[str, Any] = tomllib.loads(path.read_text(encoding="utf-8"))
    return Settings.model_validate(data)


settings = load_settings()