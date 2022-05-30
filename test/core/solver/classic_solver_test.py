import unittest

from core.board.classic_board import ClassicBoard
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
        print(solved_board.board)
