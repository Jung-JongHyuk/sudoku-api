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
