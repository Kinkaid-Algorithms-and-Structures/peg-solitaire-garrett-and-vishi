from typing import Tuple

class Player:
    def __init__(self):
        self.name: str = "player"

    def make_move(self, game):
        start, end = self.get_move()
        if game.board.is_valid_move(start, end):
            game.make_move(start, end)
        else:
            print("invalid move")

    def get_move(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        while True:
            try:
                start_x = input("Enter starting row: ")
                start_y = input("Enter starting column: ")
                end_x = input("Enter ending row: ")
                end_y = input("Enter ending column: ")

                return (start_x, start_y), (end_x, end_y)

            except ValueError:
                print("Invalid input")
