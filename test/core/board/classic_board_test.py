import unittest

from core.board.cell import Cell
from core.board.classic_board import ClassicBoard
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition


class ClassicBoardTestCase(unittest.TestCase):
    def test_init(self):
        board = ClassicBoard()
        board_row_size = len(board.board)
        board_col_size = len(board.board[0])
        self.assertEqual(board_row_size, 9)
        self.assertEqual(board_col_size, 9)

    def test_accessor(self):
        board = ClassicBoard()
        position = PlaneGridBoardPosition(rowIndex=3, colIndex=3)

        value_to_set = Cell(value=7, is_hint=False)
        board.set_value(position=position, value=value_to_set)
        value = board.get_value(position=position)

        self.assertEqual(value, value_to_set)

    def test_accessor_when_invalid_position(self):
        board = ClassicBoard()
        position = PlaneGridBoardPosition(rowIndex=-1, colIndex=10)

        with self.assertRaises(IndexError):
            value_to_set = Cell(value=7, is_hint=False)
            board.set_value(position=position, value=value_to_set)

    def test_json(self):
        board = ClassicBoard()
        json = board.write_to_json()

        board.read_from_json(json)

        board_row_size = len(board.board)
        board_col_size = len(board.board[0])
        self.assertEqual(board_row_size, 9)
        self.assertEqual(board_col_size, 9)


if __name__ == '__main__':
    unittest.main()
