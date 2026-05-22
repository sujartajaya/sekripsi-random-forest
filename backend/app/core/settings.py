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

    class Config:
        env_file = ".env"


settings = Settings()