from .role_manager import RoleManagerEntity
from dataclasses import dataclass
from typing import final

@final
@dataclass
class PermissionEntity:
    id: int
    role: RoleManagerEntity
    model: str
    get: bool
    post: bool
    put: bool
    patch: bool
    delete: bool

    def __post_init__(self):
        pass