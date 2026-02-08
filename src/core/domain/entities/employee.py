from src.core.domain.value_objects import Post
from dataclasses import dataclass
from typing import final, NewType
from uuid import UUID

EmpId = NewType('EmpId', UUID)

@final
@dataclass(frozen=True, slots=True, kw_only=True)
class EmployeeEntity:
    uuid: EmpId
    fio: str
    post: Post
    years: int
    address: str
    phone_number: str
    email: str
    salary: float

    def __post_init__(self):
        pass