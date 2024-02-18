from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ADMIN_ID: int
    BOT_TOKEN: str

    model_config = SettingsConfigDict(env_file="path_to_env_file")


config = Settings()
