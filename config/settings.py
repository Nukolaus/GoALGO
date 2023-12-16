
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = Field(..., env="POSTGRES_USER")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")
    postgres_host: str = Field("localhost", env="POSTGRES_HOST")
    postgres_port_number: int = Field(5433, env="POSTGRES_PORT_NUMBER")
    postgres_db: str = Field(..., env="POSTGRES_DB")

    access_token_expire_minutes: int = Field(
        60 * 60 * 24,
        description="Access token expire time",
        alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )

    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str = Field("HS256", alias="ALGORITHM")
    log_file:str = Field(..., env="LOG_FILE")


settings = Settings(_env_file="./config/.env")

