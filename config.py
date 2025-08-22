from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    database_password: str = Field(..., env="DATABASE_PASSWORD")
# secret_key: str = Field(..., env="SECRET_KEY")
# api_key: str = Field(..., env="API_KEY")
# redis_url: str = Field(default="redis://localhost:6379", env="REDIS_URL")
# debug: bool = Field(default=False, env="DEBUG")
# port: int = Field(default=8000, env="PORT")

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
