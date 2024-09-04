def make_board(peg_pos):
    line = ""
    for y in range(len(peg_pos)):
        for i in range(len(peg_pos[-y-1])):
            line += " "
        for x in range(len(peg_pos[y])):
            line += peg_pos[y][x]
            line += " "
        print(line)
        line = ""

def if_possible(start_pos, end_pos, peg_pos):
    if peg_pos[end_pos] == "o":
        if start_pos[]
    else:
        return False

def check_ending():
    pass
peg = [["o"],["@","@"],["@","@","@"],["@","@","@","@"],["@","@","@","@","@"]]
make_board(peg)

