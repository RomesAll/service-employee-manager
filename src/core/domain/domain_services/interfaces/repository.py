from src.core.domain.entities import EmployeeEntity, PermissionEntity, RoleManagerEntity
from abc import ABC, abstractmethod
from typing import Union
from uuid import UUID

UnionEntity = Union[EmployeeEntity, PermissionEntity, RoleManagerEntity]
UnionId = Union[UUID, int]

class IRepository(ABC):
    @abstractmethod
    def get_all(self) -> UnionEntity:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id_record: UnionId) -> UnionEntity:
        raise NotImplementedError

    @abstractmethod
    def add(self, new_record: UnionEntity) -> UnionEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self, employee_id: UnionId, employee: UnionEntity) -> UnionEntity:
        raise NotImplementedError

    @abstractmethod
    def delete(self, employee_id: UnionId) -> UnionEntity:
        raise NotImplementedError