from dataclasses import dataclass
from typing import final, ClassVar
from pydantic import ValidationError

@final
@dataclass
class Post:
    _allowed_values: ClassVar[set[str]] = {
        'backend',
        'frontend',
        'fullstack',
        'testing',
    }
    post_name: str

    def __post_init__(self):
        if self.post_name not in self._allowed_values:
            raise ValidationError(f'Post must be in: {', '.join(self._allowed_values)}')