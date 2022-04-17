import json
from dataclasses import asdict

from core.board.board import Board
from core.board.cell import Cell
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition


class ClassicBoard(Board):
    def __init__(self):
        self.row_size = 9
        self.col_size = 9
        self.box_size = 3
        self.board = [[Cell(value=None, is_hint=False)] * self.col_size] * self.row_size

    def set_value(self, position: PlaneGridBoardPosition, value: Cell) -> None:
        if self.is_position_valid(position):
            self.board[position.rowIndex][position.colIndex] = value
        else:
            raise IndexError

    def read_from_json(self, json_str: str) -> None:
        self.board = json.loads(json_str)

    def write_to_json(self) -> str:
        result = list(map(lambda row: list(map(lambda cell: asdict(cell), row)), self.board))
        return json.dumps(result)

    def get_value(self, position: PlaneGridBoardPosition) -> Cell:
        if self.is_position_valid(position):
            return self.board[position.rowIndex][position.colIndex]
        else:
            raise IndexError

    def is_position_valid(self, position: PlaneGridBoardPosition):
        return 0 <= position.rowIndex < self.row_size and 0 <= position.colIndex < self.col_size
