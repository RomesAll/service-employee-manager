from dataclasses import dataclass
from typing import final
from .role_manager import RoleId

@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PermissionEntity:
    id: int
    role: RoleId
    model: str
    get: bool
    post: bool
    put: bool
    patch: bool
    delete: bool

    def __post_init__(self):
        pass