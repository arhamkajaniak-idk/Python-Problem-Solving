# Board_2D represents the 4x4 chessboard
Board_2D = [[0 for i in range(4)] for j in range(4)]

# starting position for the first queen (Q1)
starting_position = 0


def board_reset():
    """
    Input: none
    Output: none
    What it does: sets all cells in Board_2D back to 0.
    """
    global Board_2D
    for r in range(4):
        for c in range(4):
            Board_2D[r][c] = 0


def find_next_location(starting_position):
    """
    Input: starting_position (int from 0 to 15)
    Output: index (0-15) of the next free cell, or -1 if none
    What it does: searches the board from starting_position for a 0.
    """
    global Board_2D
    pos = starting_position
    while pos < 16:
        row = pos // 4
        col = pos % 4
        if Board_2D[row][col] == 0:
            return pos
        pos += 1
    return -1


def place_queen(queen_number, starting_position=None):
    """
    Input: queen_number (int), starting_position (int or None)
    Output: position where the queen is placed, or -1
    What it does: finds a free cell and places the queen there.
    """
    global Board_2D

    if starting_position is None:
        search_start = 0
    else:
        search_start = starting_position

    pos = find_next_location(search_start)
    if pos == -1:
        return -1

    row = pos // 4
    col = pos % 4
    Board_2D[row][col] = "Q" + str(queen_number)
    set_conflict_locations(queen_number, row, col)
    return pos


def set_conflict_locations(queen_number, queen_row, queen_col):
    """
    Input: queen_number (int), queen_row (int), queen_col (int)
    Output: none
    What it does: marks all squares attacked by this queen with the queen number.
    """
    global Board_2D

    # mark same row
    for c in range(4):
        if Board_2D[queen_row][c] == 0:
            Board_2D[queen_row][c] = queen_number

    # mark same column
    for r in range(4):
        if Board_2D[r][queen_col] == 0:
            Board_2D[r][queen_col] = queen_number

    # down-right diagonal
    r = queen_row + 1
    c = queen_col + 1
    while r < 4 and c < 4:
        if Board_2D[r][c] == 0:
            Board_2D[r][c] = queen_number
        r += 1
        c += 1

    # up-right diagonal
    r = queen_row - 1
    c = queen_col + 1
    while r >= 0 and c < 4:
        if Board_2D[r][c] == 0:
            Board_2D[r][c] = queen_number
        r -= 1
        c += 1

    # down-left diagonal
    r = queen_row + 1
    c = queen_col - 1
    while r < 4 and c >= 0:
        if Board_2D[r][c] == 0:
            Board_2D[r][c] = queen_number
        r += 1
        c -= 1

    # up-left diagonal
    r = queen_row - 1
    c = queen_col - 1
    while r >= 0 and c >= 0:
        if Board_2D[r][c] == 0:
            Board_2D[r][c] = queen_number
        r -= 1
        c -= 1


def dead_end():
    """
    Input: none
    Output: none
    What it does: resets the board and moves the start position for Q1.
    """
    global starting_position
    board_reset()
    starting_position += 1


def display_board():
    """
    Input: none
    Output: none
    What it does: prints the final board in a simple way.
    """
    global Board_2D
    for row in Board_2D:
        print(row)


def main():
    """
    Input: none
    Output: none
    What it does: controls the process of placing 4 queens safely.
    """
    global starting_position
    board_reset()
    solved = False

    # try different starting positions for Q1
    while (not solved) and starting_position < 16:
        board_reset()
        failed = False

        # place queen 1 using starting_position
        pos1 = place_queen(1, starting_position)
        if pos1 == -1:
            dead_end()
            continue

        # place queens 2, 3, 4 starting from position 0
        for q in range(2, 5):
            pos_q = place_queen(q, 0)
            if pos_q == -1:
                failed = True
                break

        # if any queen failed, restart with next Q1 start
        if failed:
            dead_end()
        else:
            solved = True

    if solved:
        print("Solution found:")
        display_board()
    else:
        print("No solution")


main()
