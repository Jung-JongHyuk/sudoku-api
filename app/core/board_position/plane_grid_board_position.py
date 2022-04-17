from dataclasses import dataclass
from core.board_position.board_position import BoardPosition


@dataclass
class PlaneGridBoardPosition(BoardPosition):
    rowIndex: int
    colIndex: int
