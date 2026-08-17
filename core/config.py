from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    """Class that defines pydantic validation"""

    google_api_key: str

    model_name: str = "gemini-2.5-flash"

    embedding_model: str = (
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    chunk_size: int = 800

    chunk_overlap: int = 120

    top_k: int = 4

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()