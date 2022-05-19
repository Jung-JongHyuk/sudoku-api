import unittest

from core.board.cell import Cell
from core.board.classic_board import ClassicBoard
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition


class ClassicBoardTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.board = ClassicBoard()

    def test_init(self):
        board_row_size = len(self.board.board)
        board_col_size = len(self.board.board[0])
        self.assertEqual((board_row_size, board_col_size), (9, 9))

    def test_accessor(self):
        position = PlaneGridBoardPosition(rowIndex=3, colIndex=3)

        value_to_set = Cell(value=7, is_hint=False)
        self.board.set_value(position=position, cell=value_to_set)
        value = self.board.get_value(position=position)

        self.assertEqual(value, value_to_set)

    def test_accessor_when_invalid_position_value(self):
        with self.assertRaises(IndexError):
            value_to_set = Cell(value=7, is_hint=False)
            position = PlaneGridBoardPosition(rowIndex=-1, colIndex=10)
            self.board.set_value(position=position, cell=value_to_set)

        with self.assertRaises(ValueError):
            value_to_set = Cell(value=10, is_hint=False)
            position = PlaneGridBoardPosition(rowIndex=3, colIndex=3)
            self.board.set_value(position=position, cell=value_to_set)

    def test_json_conversion(self):
        json = self.board.write_to_json()

        self.board.read_from_json(json)

        board_row_size = len(self.board.board)
        board_col_size = len(self.board.board[0])
        self.assertEqual((board_row_size, board_col_size), (9, 9))
        self.assertTrue(isinstance(
            self.board.get_value(PlaneGridBoardPosition(rowIndex=0, colIndex=0)),
            Cell
        ))


if __name__ == '__main__':
    unittest.main()
