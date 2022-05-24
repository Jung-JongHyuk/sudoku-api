import unittest

from core.board.cell import Cell
from core.board.classic_board import ClassicBoard
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition
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

    def test_check_is_row_valid(self):
        position = PlaneGridBoardPosition(rowIndex=7, colIndex=3)

        value_to_set = Cell(value=8, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertFalse(self.checker.check_is_row_valid(self.board, position))

        value_to_set = Cell(value=1, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertTrue(self.checker.check_is_row_valid(self.board, position))

    def test_check_is_col_valid(self):
        position = PlaneGridBoardPosition(rowIndex=7, colIndex=3)

        value_to_set = Cell(value=6, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertFalse(self.checker.check_is_col_valid(self.board, position))

        value_to_set = Cell(value=1, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertTrue(self.checker.check_is_col_valid(self.board, position))

    def test_check_is_box_valid(self):
        position = PlaneGridBoardPosition(rowIndex=7, colIndex=3)

        value_to_set = Cell(value=3, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertFalse(self.checker.check_is_box_valid(self.board, position))

        value_to_set = Cell(value=1, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertTrue(self.checker.check_is_box_valid(self.board, position))

    def test_check_is_valid(self):
        self.assertTrue(self.checker.check_is_valid(self.board))

        position = PlaneGridBoardPosition(rowIndex=7, colIndex=3)
        value_to_set = Cell(value=None, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertTrue(self.checker.check_is_valid(self.board))

        value_to_set = Cell(value=2, is_hint=False)
        self.board.set_cell(position, value_to_set)
        self.assertFalse(self.checker.check_is_valid(self.board))
