from typing import Any

from core.board.board import Board
from core.board.cell import Cell
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition


class ClassicBoard(Board):
    def __init__(self):
        self.rowSize = 9
        self.colSize = 9
        self.boxSize = 3
        self.board = [[Cell(value=None, is_hint=False)] * self.colSize] * self.rowSize

    def set_value(self, position: PlaneGridBoardPosition, value: Any) -> None:
        self.board[position.rowIndex][position.colIndex] = value

    def read_from_json(self, json: str) -> None:
        pass

    def write_to_json(self) -> str:
        pass

    def get_value(self, position: PlaneGridBoardPosition) -> Any:
        return self.board[position.rowIndex][position.colIndex]