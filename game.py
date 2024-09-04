from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player()

    def start_game(self):
        self.board.initialize()
        self.player.get_player()

    def make_move(self, starting_pos, ending_pos):
        if self.board.is_valid_move(starting_pos, ending_pos):
            self.board.move_peg(starting_pos, ending_pos)
        else:
            print("Invalid move")

    def is_won(self) -> bool:
        return self.board.is_solved()

    def is_lost(self) -> bool:
        pass
