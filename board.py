from typing import List, Tuple

class Board:
    def __init__(self):
        self.layout:List[List[str]] = [["@"],["@","@"],["@","@","@"],["@","@","@","@"],["@","@","@","@","@"]]

    def set(self, pos_x, pos_y):
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        self.layout[pos_y][pos_x] = "o"

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

    def is_valid_move(self, starting_pos: Tuple[int, int], ending_pos: Tuple[int, int]) -> bool:

        if (ending_pos[0] < 0 or ending_pos[1] < 0 or
                starting_pos[0] < 0 or starting_pos[1] < 0 or
                starting_pos[0] > 4 or ending_pos[0] > 4 or
                starting_pos[0] < starting_pos[1] or ending_pos[0] < ending_pos[1]):
            return False
        if self.layout[ending_pos[0]][ending_pos[1]] == "o" and self.layout[starting_pos[0]][starting_pos[1]] == "@":
            change_y = ending_pos[0] - starting_pos[0]
            change_x = ending_pos[1] - starting_pos[1]
            if (change_x == -2 or change_x == 0 or change_x == 2) and (change_y == -2 or change_y == 0 or change_y == 2):
                if change_x == 0 or change_y == 0:
                    if change_x == 0 and change_y == 0:
                        return False
                    elif self.layout[starting_pos[0] + change_y//2][starting_pos[1] + change_x//2] == "@":
                        return True
                elif change_y/change_x != -1:
                    if self.layout[starting_pos[0] + change_y//2][starting_pos[1] + change_x//2] == "@":
                        return True
        return False


    def move_peg(self, starting_pos: Tuple[int, int], ending_pos: Tuple[int, int]):
        if self.is_valid_move(starting_pos, ending_pos):
            self.layout[ending_pos[0]][ending_pos[1]] = "@"
            self.layout[starting_pos[0]][starting_pos[1]] = "o"
            middle_y = (starting_pos[0] + ending_pos[0])//2
            middle_x = (starting_pos[1] + ending_pos[1])//2
            self.layout[middle_y][middle_x] = "o"
            self.display()

    def game_over(self) -> str:
        peg_pos = 0
        for pos_y in range(5):
            for pos_x in range(pos_y + 1):
                if self.layout[pos_y][pos_x] == "@":
                    peg_pos += 1
                    for end_pos_y in range(-2,4,2):
                        for end_pos_x in range(-2,4,2):
                            if self.is_valid_move((pos_y,pos_x),(pos_y + end_pos_y, pos_x +end_pos_x)):
                                return "continue"

        if peg_pos == 1:
            return "win"
        else:
            return "lose"

