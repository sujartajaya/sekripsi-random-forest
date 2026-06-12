from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # =========================
    # RANDOM FOREST SETTINGS
    # =========================

    N_TREES: int = 100

    MAX_DEPTH: int = 10

    MIN_SAMPLES_SPLIT: int = 2

    MIN_SAMPLES_LEAF: int = 1

    MAX_FEATURES: int = 4

    CRITERION: str = "gini"

    RANDOM_STATE: int = 42

    DEBUG: bool = True

    # Database
    DB_HOST: str = "mysql"
    DB_PORT: int = 3306
    DB_NAME: str = "autism_db"
    DB_USER: str = "root"
    DB_PASSWORD: str = "susah_diingat"

    # SMTP Settings
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    SMTP_FROM: str
    APP_URL: str

    class Config:
        env_file = ".env"


settings = Settings()