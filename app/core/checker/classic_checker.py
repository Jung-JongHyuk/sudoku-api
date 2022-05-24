from core.board.classic_board import ClassicBoard
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition
from core.checker.checker import Checker


class ClassicChecker(Checker):
    def check_is_valid(self, board: ClassicBoard, position: PlaneGridBoardPosition = None) -> bool:
        if position:
            return self.check_is_row_valid(board, position) and \
                   self.check_is_col_valid(board, position) and \
                   self.check_is_box_valid(board, position)
        else:
            for row_index in range(board.row_size):
                if not self.check_is_row_valid(board, PlaneGridBoardPosition(row_index, board.col_size - 1)):
                    return False
            for col_index in range(board.col_size):
                if not self.check_is_col_valid(board, PlaneGridBoardPosition(board.row_size - 1, col_index)):
                    return False
            for row_index in range(board.box_size - 1, board.row_size, board.box_size):
                for col_index in range(board.box_size - 1, board.col_size, board.box_size):
                    if not self.check_is_box_valid(board, PlaneGridBoardPosition(row_index, col_index)):
                        return False
            return True

    def check_is_row_valid(self, board: ClassicBoard, position: PlaneGridBoardPosition) -> bool:
        values = [board.get_value(PlaneGridBoardPosition(position.rowIndex, colIndex)).value for colIndex in
                  range(position.colIndex + 1)]
        return len(set(values)) == len(values)

    def check_is_col_valid(self, board: ClassicBoard, position: PlaneGridBoardPosition) -> bool:
        values = [board.get_value(PlaneGridBoardPosition(rowIndex, position.colIndex)).value for rowIndex in
                  range(position.rowIndex + 1)]
        return len(set(values)) == len(values)

    def check_is_box_valid(self, board: ClassicBoard, position: PlaneGridBoardPosition) -> bool:
        box_start_row_index = int(position.rowIndex / board.row_size) * board.box_size
        box_start_col_index = int(position.colIndex / board.col_size) * board.box_size
        values = [board.get_value(PlaneGridBoardPosition(rowIndex, colIndex)).value
                  for rowIndex in range(box_start_row_index, box_start_row_index + board.box_size)
                  for colIndex in range(box_start_col_index, box_start_col_index + board.box_size)]
        return len(set(values)) == len(values)
