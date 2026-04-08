"""
Configuration module for telemetry dashboard.

Handles environment configuration for runtime behavior.
Centralizing configuration improves maintainability
and supports container deployment flexibility.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application runtime settings.

    Attributes:
        app_name: Application display name.
        refresh_interval_seconds: Dashboard refresh rate.
    """

    app_name: str = "System Health Telemetry Dashboard"
    refresh_interval_seconds: int = 5

    class Config:
        """Environment variable configuration."""

        env_file = ".env"
        extra = "ignore"


settings = Settings()