from typing import *
from board import Board

class Player:
    def __init__(self):
        self.name: str = "player"


    def get_move(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        while True:
            try:
                start_r = int(input("Enter starting row: "))
                start_c = int(input("Enter starting column: "))
                end_r = int(input("Enter ending row: "))
                end_c = int(input("Enter ending column: "))

                return (start_r, start_c), (end_r, end_c)

            except ValueError:
                print("Invalid input")
