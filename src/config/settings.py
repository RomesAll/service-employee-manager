from pydantic_settings import BaseSettings
from .broker import BrokerSettings
from .redis import RedisSettings
from .database import DatabaseSettings
from .logging_conf import *

class Settings(BaseSettings):
    # broker: BrokerSettings = BrokerSettings()
    # redis: RedisSettings = RedisSettings()
    database: DatabaseSettings = DatabaseSettings()

settings = Settings()