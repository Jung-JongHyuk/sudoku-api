from dataclasses import dataclass
from typing import Any


@dataclass
class Cell:
    value: Any
    is_hint: bool
