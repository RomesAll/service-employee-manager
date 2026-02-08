from src.core.domain.domain_services.dto.role_manager import PostRoleManagerDto, UpdateRoleManagerDto
from src.core.domain.entities import RoleManagerEntity
from abc import ABC, abstractmethod

class RoleManagerRepository(ABC):
    @abstractmethod
    def get_all(self) -> RoleManagerEntity:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, role_manager_id: int) -> RoleManagerEntity:
        raise NotImplementedError

    @abstractmethod
    def add_role_manager(self, role_manager: PostRoleManagerDto) -> RoleManagerEntity:
        raise NotImplementedError

    @abstractmethod
    def update_role_manager(self, role_manager_id: int, role_manager: UpdateRoleManagerDto) -> RoleManagerEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_role_manager(self, role_manager_id: int) -> RoleManagerEntity:
        raise NotImplementedError