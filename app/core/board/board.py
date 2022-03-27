from abc import *
from typing import Type, Any

from core.board_position.board_position import BoardPosition


class Board(metaclass=ABCMeta):
    @abstractmethod
    def get_position_class(self) -> Type[BoardPosition]:
        pass

    @abstractmethod
    def get_value(self, position: BoardPosition) -> Any:
        pass

    @abstractmethod
    def set_value(self, position: BoardPosition, value: Any) -> None:
        pass

    @abstractmethod
    def read_from_json(self, json: str) -> None:
        pass

    @abstractmethod
    def write_to_json(self) -> str:
        pass