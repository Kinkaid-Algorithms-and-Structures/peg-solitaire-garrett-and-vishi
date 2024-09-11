from typing import *

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
                    self.board.layout[empty_r][empty_c] = "o"
                    break
                else:
                    print("Invalid row or column, please try again.")
            except ValueError:
                    print("Please enter an integer")

    def make_move(self, starting_pos: Tuple[int,int], ending_pos: Tuple[int,int]):
        self.board.move_peg(starting_pos, ending_pos)


    def play(self):
        self.start_game()
        self.board.display()
        while self.board.is_game_over() == "continue":
            start_end = self.player.get_move()
            start = start_end[0]
            end = start_end[1]
            self.make_move(start, end)
        if self.board.is_game_over() == "win":
            print("you won!")
        elif self.board.is_game_over() == "lose":
            print("you lost!")