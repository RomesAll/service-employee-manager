from src.core.domain.entities import EmployeeEntity
from src.core.domain.value_objects import Role
from datetime import datetime
from pydantic import BaseModel

class PostRoleManagerDto(BaseModel):
    employee: EmployeeEntity
    role: Role
    login: str
    password: bytes

class GetRoleManagerDto(PostRoleManagerDto):
    id: int
    created_at: datetime
    updated_at: datetime

class UpdateRoleManagerDto(PostRoleManagerDto):
    pass