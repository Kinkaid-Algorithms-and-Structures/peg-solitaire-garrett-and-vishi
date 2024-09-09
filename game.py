from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player()

    def start_game(self):
        while True:
            try:
                empty_r = int(input("Which row is the hole you want to leave empty?"))
                empty_c = int(input("Which column is the hole you want to leave empty?"))
                if 0<=empty_r<5 and 0<=empty_c<5:
                    self.board.layout[empty_r][empty_c] = " "
                    break
                else:
                    print("Invalid row or column, please try again.")
            except ValueError:
                    print("Please enter an integer")

    def make_move(self, starting_pos, ending_pos):
        if self.board.is_valid_move(starting_pos, ending_pos):
            self.board.move_peg(starting_pos, ending_pos)
        else:
            print("Invalid move")

    def play(self):
        self.start_game()
        while self.board.is_game_over() == "continue":
            self.player.get_move()
        if self.board.is_game_over() == "win":
            print("you won!")
        elif self.board.is_game_over() == "lose":
            print("you lost!")