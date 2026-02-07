from pydantic_settings import BaseSettings
from broker import BrokerSettings
from redis import RedisSettings
from database import DatabaseSettings
import logging_conf

class Settings(BaseSettings):
    broker: BrokerSettings = BrokerSettings()
    redis: RedisSettings = RedisSettings()
    database: DatabaseSettings = DatabaseSettings()

settings = Settings()
print(settings.database.get_database_url_sync)