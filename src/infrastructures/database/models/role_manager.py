from sqlalchemy import ForeignKey
from .base import Base, mapped_column, Mapped

class RoleManagerOrm(Base):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    employee: Mapped[int] = mapped_column(ForeignKey('employeeorm.id', ondelete='CASCADE'), nullable=False)
    role: Mapped[str]
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[bytes]