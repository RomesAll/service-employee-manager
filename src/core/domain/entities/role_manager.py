from src.core.domain.value_objects import Role
from .employee import EmployeeEntity
from dataclasses import dataclass
from .employee import EmpId
from typing import final, NewType

RoleId = NewType('RoleId', int)

@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RoleManagerEntity:
    id: int
    employee: EmpId
    role: Role
    login: str
    password: str

    def __post_init__(self):
        pass