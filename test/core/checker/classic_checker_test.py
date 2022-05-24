import unittest

from core.board.classic_board import ClassicBoard
from core.checker.classic_checker import ClassicChecker


class ClassicCheckerTest(unittest.TestCase):
    board = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.classic_sudoku_file_path = '../../resource/classic_sudoku.json'
        cls.board = ClassicBoard()
        cls.checker = ClassicChecker()

    def setUp(self) -> None:
        with open(self.classic_sudoku_file_path, 'r') as file:
            json_str = file.read()
            self.board.read_from_json(json_str)
