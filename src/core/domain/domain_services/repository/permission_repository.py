from src.core.domain.domain_services.dto.permission import PostPermissionDto, UpdatePermissionDto
from src.core.domain.entities import PermissionEntity
from abc import ABC, abstractmethod

class PermissionRepository(ABC):
    @abstractmethod
    def get_all(self) -> PermissionEntity:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, permission_id: int) -> PermissionEntity:
        raise NotImplementedError

    @abstractmethod
    def add_permission(self, permission: PostPermissionDto) -> PermissionEntity:
        raise NotImplementedError

    @abstractmethod
    def update_permission(self, permission_id: int, permission: UpdatePermissionDto) -> PermissionEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_permission(self, permission_id: int) -> PermissionEntity:
        raise NotImplementedError