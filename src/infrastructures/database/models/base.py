from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import text
from datetime import datetime, timezone

def get_utc_time():
    return datetime.now(tz=timezone.utc)

class Base(DeclarativeBase):
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=get_utc_time)

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return  cls.__name__.lower()