from pydantic_settings import BaseSettings, SettingsConfigDict

class BrokerSettings(BaseSettings):
    BROKER_HOST: str
    BROKER_PORT: int
    BROKER_USER: str
    BROKER_PASSWORD: str
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    @property
    def get_database_url_sync(self):
        return (f'amqp://{self.BROKER_USER}:{self.BROKER_PASSWORD}'
                f'@{self.BROKER_HOST}:{self.BROKER_PORT}/')
