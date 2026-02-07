from src.core.domain.value_objects import Role
from .employee import EmployeeEntity
from dataclasses import dataclass
from typing import final

@final
@dataclass
class RoleManagerEntity:
    id: int
    employee: EmployeeEntity
    role: Role
    login: str
    password: str

    def __post_init__(self):
        pass