import unittest
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

        value_to_set = 7
        board.set_value(position=position, value=value_to_set)
        value = board.get_value(position=position)

        self.assertEqual(value, value_to_set)

    def test_accessor_when_invalid_position(self):
        board = ClassicBoard()
        position = PlaneGridBoardPosition(rowIndex=-1, colIndex=10)

        value_to_set = 7
        board.set_value(position=position, value=value_to_set)
        self.assertRaises(IndexError)



if __name__ == '__main__':
    unittest.main()
