from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from base import Base

class PermissionOrm(Base):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    role: Mapped[int] = mapped_column(ForeignKey('rolemanagerorm.id', ondelete='CASCADE'), nullable=False)
    model: Mapped[str]
    get: Mapped[bool] = mapped_column(default=False)
    post: Mapped[bool] = mapped_column(default=False)
    put: Mapped[bool] = mapped_column(default=False)
    patch: Mapped[bool] = mapped_column(default=False)
    delete: Mapped[bool] = mapped_column(default=False)