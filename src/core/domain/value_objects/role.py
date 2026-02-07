from dataclasses import dataclass
from typing import final, ClassVar
from pydantic import ValidationError

@final
@dataclass
class Role:
    _allowed_values: ClassVar[set[str]] = {
        'admin',
        'manager',
        'guest',
    }
    role_name: str

    def __post_init__(self):
        if self.role_name not in self._allowed_values:
            raise ValidationError(f'Role name must be in: {', '.join(self._allowed_values)}')