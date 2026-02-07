from datetime import datetime
from pydantic import BaseModel
from uuid import UUID
from src.core.domain.value_objects import Post

class PostEmployeeDto(BaseModel):
    uuid: UUID
    fio: str
    post: Post
    years: int
    address: str
    phone_number: str
    email: str
    salary: float

class GetEmployeeDto(PostEmployeeDto):
    created_at: datetime
    updated_at: datetime

class UpdateEmployeeDto(BaseModel):
    pass