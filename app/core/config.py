from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PINECONE_API_KEY: str
    PINECONE_ENVIRONMENT: str
    PINECONE_INDEX: str
    GROQ_API_KEY: str
    OPENAI_API_KEY: str
    HUGGINGFACE_MODEL: str

    class Config:
        env_file = ".env"

settings = Settings()