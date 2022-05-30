import copy
from typing import Optional

from core.board.classic_board import ClassicBoard
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition
from core.checker.classic_checker import ClassicChecker
from core.solver.solver import Solver


class ClassicSolver(Solver):
    def __init__(self):
        self.row_size = None
        self.col_size = None
        self.checker = ClassicChecker()

    def solve_sudoku(self, board: ClassicBoard) -> Optional[ClassicBoard]:
        self.row_size = board.row_size
        self.col_size = board.col_size
        solved_board = copy.deepcopy(board)
        is_answer_exist = self.solve_cell(solved_board, PlaneGridBoardPosition(0, 0))
        return solved_board if is_answer_exist else None

    def solve_cell(self, board: ClassicBoard, position: Optional[PlaneGridBoardPosition]) -> bool:
        if not position:
            return self.checker.check_is_valid(board)

        cell = board.get_cell(position)
        if cell.is_hint:
            return self.solve_cell(board, self.get_next_position(position))
        else:
            for value in board.possible_values:
                cell.value = value
                board.set_cell(position, cell)
                if self.checker.check_is_valid(board, position):
                    if self.solve_cell(board,
                                       self.get_next_position(position)):
                        return True
            return False

    def get_next_position(self, position: PlaneGridBoardPosition) -> Optional[PlaneGridBoardPosition]:
        if position.colIndex == self.col_size - 1:
            if position.rowIndex == self.row_size - 1:
                return None
            else:
                return PlaneGridBoardPosition(position.rowIndex + 1, 0)
        else:
            return PlaneGridBoardPosition(position.rowIndex, position.colIndex + 1)
