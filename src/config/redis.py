from pydantic_settings import BaseSettings, SettingsConfigDict

class CacheSettings(BaseSettings):
    REDIS_CACHE_PREFIX: str
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_USER: str
    REDIS_PASSWORD: str
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    @property
    def get_redis_url(self):
        return (f'redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}'
                f'@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}')

