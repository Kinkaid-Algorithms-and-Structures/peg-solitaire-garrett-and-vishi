from typing import List, Tuple

class Board:
    def __init__(self):
        self.layout:List[List[int]] = []

    def display(self):
        pass

    def move_peg(self, starting_pos: Tuple[int, int], ending_pos: Tuple[int, int]):
        pass

    def is_valid_move(self, starting_pos: Tuple[int, int], ending_pos: Tuple[int, int]) -> bool:
        pass

    def is_solved(self) -> bool:
        pass