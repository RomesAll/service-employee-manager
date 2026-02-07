from src.core.domain.domain_services import EmployeeRepository
from src.core.domain.domain_services.employee.dto.employee import UpdateEmployeeDto, PostEmployeeDto, GetEmployeeDto
from uuid import UUID

class EmployeeService:
    def __init__(self, repository: EmployeeRepository):
        self.employee_repository = repository

    def get_employee_by_id(self, employee_id: UUID) -> GetEmployeeDto:
        employee = self.employee_repository.get_by_id(employee_id)
        return employee

    def get_all_employee(self) -> list[GetEmployeeDto]:
        employee_list = self.employee_repository.get_all()
        return employee_list

    def add(self, employee: PostEmployeeDto) -> GetEmployeeDto:
        employee = self.employee_repository.add_employee(employee)
        return employee

    def update(self, employee_id: UUID, employee: UpdateEmployeeDto) -> GetEmployeeDto:
        employee = self.employee_repository.update_employee(employee_id, employee)
        return employee

    def delete(self, employee_id: UUID) -> GetEmployeeDto:
        employee = self.employee_repository.delete_employee(employee_id)
        return employee