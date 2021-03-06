from abc import *

from core.board.board import Board


class Solver(metaclass=ABCMeta):
    @abstractmethod
    def solve_sudoku(self, board: Board) -> Board:
        pass

    @abstractmethod
    def check_is_answer_unique(self, board: Board) -> bool:
        pass
