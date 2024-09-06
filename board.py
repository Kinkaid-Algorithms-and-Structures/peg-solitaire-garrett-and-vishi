from typing import List, Tuple

class Board:
    def __init__(self):
        self.layout:List[List[str]] = [["o"],["@","@"],["@","@","@"],["@","@","@","@"],["@","@","@","@","@"]]

    def display(self):
        line = ""
        for y in range(len(self.layout)):
            for i in range(len(self.layout[-y - 1])):
                line += " "
            for x in range(len(self.layout[y])):
                line += self.layout[y][x]
                line += " "
            print(line)
            line = ""

    def move_peg(self, starting_pos: Tuple[int, int], ending_pos: Tuple[int, int]):
        pass

    def is_valid_move(self, starting_pos: Tuple[int, int], ending_pos: Tuple[int, int]) -> bool:
        if self.layout[ending_pos[0]][ending_pos[1]] == "o":
            change_y = ending_pos[0] - starting_pos[0]
            change_x = ending_pos[1] - starting_pos[1]
            if change_x == -2 or 0 or 2 and change_y == -2 or 0 or 2:
                if change_x == 0 or change_y == 0:
                    if change_x == 0 and change_y == 0:
                        return False
                elif change_y/change_x != -1:
                    if self.layout[starting_pos[0] + change_y//2][starting_pos[1] + change_x//2] == "@":
                        return True
        else:
            return False

    def is_solved(self) -> bool:
        pass


board = Board()
board.display()