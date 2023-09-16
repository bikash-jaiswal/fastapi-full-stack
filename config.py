from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    mongodb_pass: str
    open_api_key: str = "asasasasas"


settings = Settings()
