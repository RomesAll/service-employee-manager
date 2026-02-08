from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings
from typing import Final

engine: Final = create_engine(url=settings.database.get_database_url_sync)
session_factory: Final = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)