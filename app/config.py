from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    MY_API_KEY: str = 'MY_API_KEY'
    GEMINI_API_KEY: str = 'GEMINI_API_KEY'
    SYSTEM_INSTRUCTION: str = "SYSTEM_INSTRUCTION"
    GROQ_API_KEY: str = 'GROQ_API_KEY'
    OPENAI_API_KEY: str = 'OPENAI_API_KEY'

    class Config:
        env_file = ".env"


settings = Settings()
