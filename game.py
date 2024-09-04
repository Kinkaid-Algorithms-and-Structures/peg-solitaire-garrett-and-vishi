from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player()

    def start_game(self):
        self.player.get_player()
        self.board.get_board()

    def make_move(self, starting_pos, ending_pos):
        if self.board.is_valid_move(starting_pos, ending_pos):
            self.board.move_peg(starting_pos, ending_pos)
        else:
            print("Invalid move")

    def is_won(self) -> bool:
        if self.board.is_solved():
            if len(self.board.layout) == 1:
                return True
            return False


    def is_lost(self) -> bool:
        if self.is_won() == False:
            return True
        return False