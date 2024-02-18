from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ADMIN_ID: int
    BOT_TOKEN: str

    model_config = SettingsConfigDict(env_file="../.env") # The .env file is located in the root directory


config = Settings()
