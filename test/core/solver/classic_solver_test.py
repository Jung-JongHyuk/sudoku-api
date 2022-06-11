import itertools
import random
import unittest

from core.board.classic_board import ClassicBoard
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition
from core.solver.classic_solver import ClassicSolver


class ClassicSolverTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.classic_sudoku_file_path = '../../resource/classic_sudoku.json'
        cls.board = ClassicBoard()
        cls.solver = ClassicSolver()

    def setUp(self) -> None:
        with open(self.classic_sudoku_file_path, 'r') as file:
            json_str = file.read()
            self.board.read_from_json(json_str)

    def test_solve_sudoku(self):
        solved_board = self.solver.solve_sudoku(self.board)
        self.assertEqual(solved_board, self.board)

    def test_solve_invalid_sudoku(self):
        position = PlaneGridBoardPosition(3, 3)
        cell = self.board.get_cell(position)
        cell.value = 7
        self.board.set_cell(position, cell)
        solved_board = self.solver.solve_sudoku(self.board)
        self.assertEqual(solved_board, None)

    def test_is_answer_unique(self):
        self.assertTrue(self.solver.check_is_answer_unique(self.board))

        self.make_board_answer_not_unique()
        self.assertFalse(self.solver.check_is_answer_unique(self.board))

    def make_board_answer_not_unique(self):
        for (row_index, col_index) in itertools.product(range(self.board.row_size),
                                                        range(self.board.col_size)):
            position = PlaneGridBoardPosition(row_index, col_index)
            cell = self.board.get_cell(position)
            cell.is_hint = True
            self.board.set_cell(position, cell)

        idx_to_unhint = list(itertools.product(range(self.board.row_size),
                                               range(self.board.col_size)))
        random.shuffle(idx_to_unhint)
        # unhint cell의 수가 65개 이상인 classic sudoku는 여러 답을 갖는다는 것이 증명되어 있음
        for (row_index, col_index) in idx_to_unhint[:65]:
            position = PlaneGridBoardPosition(row_index, col_index)
            cell = self.board.get_cell(position)
            cell.is_hint = False
            self.board.set_cell(position, cell)
