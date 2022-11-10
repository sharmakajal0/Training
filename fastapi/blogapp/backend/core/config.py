import os

class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    SECRET_KEY = "SECRET_KEY"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    TEST_USER_EMAIL = "test@example.com"

settings = Settings()