from typing import Any

from core.board.board import Board
from core.board_position.plane_grid_board_position import PlaneGridBoardPosition


class ClassicBoard(Board):
    def set_value(self, position: PlaneGridBoardPosition, value: Any) -> None:
        pass

    def read_from_json(self, json: str) -> None:
        pass

    def write_to_json(self) -> str:
        pass

    def get_value(self, position: PlaneGridBoardPosition) -> Any:
        pass