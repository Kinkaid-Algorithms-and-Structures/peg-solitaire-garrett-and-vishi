from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player()

    def start_game(self):
        empty_r = input("Which row is the hole you want to leave empty?")
        empty_c = input("Which column is the hole you want to leave empty?")
        self.board.set(empty_r, empty_c)

    def make_move(self, starting_pos, ending_pos):
        if self.board.is_valid_move(starting_pos, ending_pos):
            self.board.move_peg(starting_pos, ending_pos)
        else:
            print("Invalid move")

    def play(self):
        self.start_game()
        while self.board.game_over() == "continue":
            self.player.make_move(self)
        if self.game.board.game_over() == "win":
            print("you won!")
        elif self.game.board.game_over() == "lose":
            print("you lost!")