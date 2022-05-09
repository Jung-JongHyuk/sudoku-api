from abc import *

from core.board.board import Board
from core.board_position.board_position import BoardPosition


class Checker(metaclass=ABCMeta):
    @abstractmethod
    def check_is_valid(self, board: Board, position: BoardPosition = None) -> bool:
        pass
