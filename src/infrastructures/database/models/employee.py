from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column

class EmployeeOrm(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    fio: Mapped[str] = mapped_column(unique=True)
    post: Mapped[str]
    years: Mapped[int]
    address: Mapped[str]
    phone_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    salary: Mapped[float] = mapped_column(default=0)