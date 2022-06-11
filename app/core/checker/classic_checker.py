import itertools

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
        values = []
        for col_index in range(board.col_size):
            cell = board.get_cell(PlaneGridBoardPosition(position.rowIndex, col_index))
            if col_index <= position.colIndex or cell.is_hint:
                values.append(cell.value)

        return len(set(values)) == len(values)

    def check_is_col_valid(self, board: ClassicBoard, position: PlaneGridBoardPosition) -> bool:
        values = []
        for row_index in range(board.row_size):
            cell = board.get_cell(PlaneGridBoardPosition(row_index, position.colIndex))
            if row_index <= position.rowIndex or cell.is_hint:
                values.append(cell.value)
        return len(set(values)) == len(values)

    def check_is_box_valid(self, board: ClassicBoard, position: PlaneGridBoardPosition) -> bool:
        box_start_row_index = int(position.rowIndex / board.box_size) * board.box_size
        box_start_col_index = int(position.colIndex / board.box_size) * board.box_size
        values = []
        for (row_index, col_index) in itertools.product(
                range(box_start_row_index, box_start_row_index + board.box_size),
                range(box_start_col_index, box_start_col_index + board.box_size)):
            curr_position = PlaneGridBoardPosition(row_index, col_index)
            cell = board.get_cell(curr_position)
            if row_index < position.rowIndex or \
                    (position.rowIndex == row_index and col_index <= position.colIndex):
                values.append(cell.value)
            elif cell.is_hint:
                values.append(cell.value)

        return len(set(values)) == len(values)
