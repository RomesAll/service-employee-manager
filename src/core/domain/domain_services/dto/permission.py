from src.core.domain.entities import RoleManagerEntity
from pydantic import BaseModel
from datetime import datetime

class PostPermissionDto(BaseModel):
    role: RoleManagerEntity
    model: str
    get: bool
    post: bool
    put: bool
    patch: bool
    delete: bool

class GetPermissionDto(PostPermissionDto):
    id: int
    created_at: datetime
    updated_at: datetime

class UpdatePermissionDto(PostPermissionDto):
    pass