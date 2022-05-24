from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Cell:
    value: Optional[Any]
    is_hint: bool
