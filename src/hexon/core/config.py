
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow", env_file_encoding="utf-8")
    PROJECT_NAME: str = "Hexon"
    API_V1_STR: str = "/api"


settings = Settings()