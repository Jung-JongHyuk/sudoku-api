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

    def check_is_answer_unique(self, board: ClassicBoard) -> bool:
        self.row_size = board.row_size
        self.col_size = board.col_size
        solved_board = copy.deepcopy(board)
        reverse_solved_board = copy.deepcopy(board)

        is_answer_exist = self.solve_cell(solved_board, PlaneGridBoardPosition(0, 0), False)
        self.solve_cell(reverse_solved_board, PlaneGridBoardPosition(0, 0), True)
        return is_answer_exist and solved_board == reverse_solved_board

    def solve_cell(self, board: ClassicBoard, position: Optional[PlaneGridBoardPosition], reverse=False) -> bool:
        if not position:
            return self.checker.check_is_valid(board)

        cell = board.get_cell(position)
        possible_values = reversed(board.possible_values) if reverse else board.possible_values
        if cell.is_hint:
            return self.solve_cell(board, self.get_next_position(position), reverse)

        for value in possible_values:
            cell.value = value
            board.set_cell(position, cell)
            if not self.checker.check_is_valid(board, position):
                continue
            if self.solve_cell(board,
                               self.get_next_position(position),
                               reverse):
                return True
        return False

    def get_next_position(self, position: PlaneGridBoardPosition) -> Optional[PlaneGridBoardPosition]:
        if position.col_index == self.col_size - 1:
            if position.row_index == self.row_size - 1:
                return None
            else:
                return PlaneGridBoardPosition(position.row_index + 1, 0)
        else:
            return PlaneGridBoardPosition(position.row_index, position.col_index + 1)
