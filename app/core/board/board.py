from abc import *
from typing import Any

from core.board_position.board_position import BoardPosition


class Board(metaclass=ABCMeta):
    possible_values: list[Any]

    @abstractmethod
    def get_cell(self, position: BoardPosition) -> Any:
        pass

    @abstractmethod
    def set_cell(self, position: BoardPosition, cell: Any) -> None:
        pass

    @abstractmethod
    def read_from_json(self, json: str) -> None:
        pass

    @abstractmethod
    def write_to_json(self) -> str:
        pass

    @abstractmethod
    def is_position_valid(self, position: BoardPosition) -> bool:
        pass

    @abstractmethod
    def is_value_valid(self, value: Any):
        pass

    def __eq__(self, other):
        return hasattr(other, '__dict__') and self.__dict__ == other.__dict__
