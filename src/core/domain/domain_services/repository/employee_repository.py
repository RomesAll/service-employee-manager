from src.core.domain.domain_services.dto.employee import UpdateEmployeeDto, PostEmployeeDto
from src.core.domain.entities import EmployeeEntity
from abc import ABC, abstractmethod
from uuid import UUID

class EmployeeRepository(ABC):
    @abstractmethod
    def get_all(self) -> EmployeeEntity:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, employee_id: UUID) -> EmployeeEntity:
        raise NotImplementedError

    @abstractmethod
    def add_employee(self, employee: PostEmployeeDto) -> EmployeeEntity:
        raise NotImplementedError

    @abstractmethod
    def update_employee(self, employee_id: UUID, employee: UpdateEmployeeDto) -> EmployeeEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_employee(self, employee_id: UUID) -> EmployeeEntity:
        raise NotImplementedError