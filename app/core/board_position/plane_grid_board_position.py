from dataclasses import dataclass

from core.board_position.board_position import BoardPosition


@dataclass
class PlaneGridBoardPosition(BoardPosition):
    row_index: int
    col_index: int
