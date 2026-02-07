from src.core.domain.value_objects import Post
from dataclasses import dataclass
from typing import final
from uuid import UUID

@final
@dataclass
class EmployeeEntity:
    uuid: UUID
    fio: str
    post: Post
    years: int
    address: str
    phone_number: str
    email: str
    salary: float

    def __post_init__(self):
        pass