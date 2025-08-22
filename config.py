from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    database_user: str = Field(..., env="DATABASE_USER")
    database_password: str = Field(..., env="DATABASE_PASSWORD")
    database_host: str = Field("localhost", env="DATABASE_HOST")
    database_port: int = Field(5432, env="DATABASE_PORT")
    database_name: str = Field(..., env="DATABASE_NAME")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()


# # Load variables from .env file into environment
# load_dotenv()

# DB_USER = os.getenv("DATABASE_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DATABASE_HOST")
# DB_PORT = os.getenv("DB_PORT", "5432")
# DB_NAME = os.getenv("DATABASE_NAME")

# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
