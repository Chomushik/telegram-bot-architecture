from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_ID: int

    model_config = SettingsConfigDict(env_file="path_to_env_file")


config = Settings()