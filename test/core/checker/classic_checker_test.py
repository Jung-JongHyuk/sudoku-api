import unittest

from core.board.classic_board import ClassicBoard


class ClassicCheckerTest(unittest.TestCase):
    board = None

    @classmethod
    def setUpClass(cls) -> None:
        classic_sudoku_file_path = '../../resource/classic_sudoku.json'
        with open(classic_sudoku_file_path, 'r') as file:
            json_str = file.read()
            cls.board = ClassicBoard()
            cls.board.read_from_json(json_str)
