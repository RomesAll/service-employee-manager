from src.core.domain.domain_services import RoleManagerRepository
from src.core.domain.domain_services.role_manager.dto.role_manager import (GetRoleManagerDto,
                                                                           PostRoleManagerDto,
                                                                           UpdateRoleManagerDto)

class RoleManagerService:
    def __init__(self, repository: RoleManagerRepository):
        self.role_manager_repository = repository

    def get_role_manager_by_id(self, role_manager_id: int) -> GetRoleManagerDto:
        role_manager = self.role_manager_repository.get_by_id(role_manager_id)
        return role_manager

    def get_all_role_manager(self) -> list[GetRoleManagerDto]:
        role_manager_list = self.role_manager_repository.get_all()
        return role_manager_list

    def add(self, role_manager: PostRoleManagerDto) -> GetRoleManagerDto:
        role_manager = self.role_manager_repository.add_role_manager(role_manager)
        return role_manager

    def update(self, role_manager_id: int, role_manager: UpdateRoleManagerDto) -> GetRoleManagerDto:
        role_manager = self.role_manager_repository.update_role_manager(role_manager_id, role_manager)
        return role_manager

    def delete(self, role_manager_id: int) -> GetRoleManagerDto:
        role_manager = self.role_manager_repository.delete_role_manager(role_manager_id)
        return role_manager