import json
from copy import copy
from dataclasses import asdict
from typing import Any

from core.board.board import Board
from core.board.cell import Cell
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition


class ClassicBoard(Board):
    def __init__(self):
        self.row_size = 9
        self.col_size = 9
        self.box_size = 3
        self.possible_values = list(range(10))
        self.board = [[Cell(value=None, is_hint=False)] * self.col_size] * self.row_size

    def set_cell(self, position: PlaneGridBoardPosition, cell: Cell) -> None:
        if self.is_position_valid(position):
            if self.is_value_valid(cell.value):
                self.board[position.rowIndex][position.colIndex] = copy(cell)
            else:
                raise ValueError
        else:
            raise IndexError

    def read_from_json(self, json_str: str) -> None:
        board_dict = json.loads(json_str)
        self.board = list(
            map(lambda row: list(
                map(lambda cell_dict: Cell(**cell_dict),
                    row)),
                board_dict
                )
        )

    def write_to_json(self) -> str:
        result = list(map(lambda row: list(map(lambda cell: asdict(cell), row)), self.board))
        return json.dumps(result)

    def get_cell(self, position: PlaneGridBoardPosition) -> Cell:
        if self.is_position_valid(position):
            return copy(self.board[position.rowIndex][position.colIndex])
        else:
            raise IndexError

    def is_position_valid(self, position: PlaneGridBoardPosition) -> bool:
        return 0 <= position.rowIndex < self.row_size and 0 <= position.colIndex < self.col_size

    def is_value_valid(self, value: Any) -> bool:
        return not value or isinstance(value, int) and 0 <= value <= 9
