from src.core.domain.domain_services import PermissionRepository
from src.core.domain.domain_services.dto.permission import GetPermissionDto, PostPermissionDto, UpdatePermissionDto

class PermissionService:
    def __init__(self, repository: PermissionRepository):
        self.permission_repository = repository

    def get_permission_by_id(self, permission_id: int) -> GetPermissionDto:
        permission = self.permission_repository.get_by_id(permission_id)
        return permission

    def get_all_permission(self) -> list[GetPermissionDto]:
        permission_list = self.permission_repository.get_all()
        return permission_list

    def add(self, permission: PostPermissionDto) -> GetPermissionDto:
        permission = self.permission_repository.add_permission(permission)
        return permission

    def update(self, permission_id: int, permission: UpdatePermissionDto) -> GetPermissionDto:
        permission = self.permission_repository.update_permission(permission_id, permission)
        return permission

    def delete(self, permission_id: int) -> GetPermissionDto:
        permission = self.permission_repository.delete_permission(permission_id)
        return permission