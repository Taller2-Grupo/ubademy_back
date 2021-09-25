from pydantic import BaseSettings


class Settings(BaseSettings):
    db_connection_string: str = "postgresql://postgres:postgres@localhost/postgres"


settings = Settings()
