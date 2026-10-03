from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "TaskHub"
    database_url: str = "sqlite:///./taskhub.db"
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 30


settings = Settings()