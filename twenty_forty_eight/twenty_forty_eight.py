"""
Christian Felt
December 27, 2019
Solves the 2048 problem on Kattis.
"""


class Tile():
    """Represent a playing tile."""

    def __init__(self, number, merged=False):
        self.number = number
        self.merged = merged


def display_board(board):
    """Print the numerical values and arrangement of tiles on the board."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j].number, end=" ")
        print("")


def reset_merged_markers(board):
    """Set all merged instance variables to False."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j].merged = False


def do_move(move, board):
    """Do a single move of the 2048 game."""
    reset_merged_markers(board)
    if move == 0:  # Left
        did_swap = True
        while did_swap:
            did_swap = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j == 0:
                        pass
                    elif board[i][j - 1].number == 0 and board[i][j].number != 0:
                        board[i][j - 1] = board[i][j]
                        board[i][j] = Tile(0, False)
                        did_swap = True
                    elif board[i][j - 1].number == board[i][j].number and board[i][j - 1].merged is False and board[i][
                        j].merged is False:
                        board[i][j - 1] = Tile(board[i][j - 1].number + board[i][j].number, True)
                        board[i][j] = Tile(0, False)
                        did_swap = True
    elif move == 1:  # Up
        did_swap = True
        while did_swap:
            did_swap = False
            for j in range(len(board[0])):
                for i in range(len(board)):
                    if i == 0:
                        pass
                    elif board[i - 1][j].number == 0 and board[i][j].number != 0:
                        board[i - 1][j] = board[i][j]
                        board[i][j] = Tile(0, False)
                        did_swap = True
                    elif board[i - 1][j].number == board[i][j].number and board[i - 1][j].merged is False and board[i][
                        j].merged is False:
                        board[i - 1][j] = Tile(board[i - 1][j].number + board[i][j].number, True)
                        board[i][j] = Tile(0, False)
                        did_swap = True
    elif move == 2:  # Right
        did_swap = True
        while did_swap:
            did_swap = False
            for i in range(len(board)):
                for j in range(len(board[0]) - 1, -1, -1):
                    if j == len(board[0]) - 1:
                        pass
                    elif board[i][j + 1].number == 0 and board[i][j].number != 0:
                        board[i][j + 1] = board[i][j]
                        board[i][j] = Tile(0, False)
                        did_swap = True
                    elif board[i][j + 1].number == board[i][j].number and board[i][j + 1].merged is False and board[i][
                        j].merged is False:
                        board[i][j + 1] = Tile(board[i][j + 1].number + board[i][j].number, True)
                        board[i][j] = Tile(0, False)
                        did_swap = True
    elif move == 3:  # Down
        did_swap = True
        while did_swap:
            did_swap = False
            for j in range(len(board[0])):
                for i in range(len(board) - 1, -1, -1):
                    if i == len(board) - 1:
                        pass
                    elif board[i + 1][j].number == 0 and board[i][j].number != 0:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = Tile(0, False)
                        did_swap = True
                    elif board[i + 1][j].number == board[i][j].number and board[i + 1][j].merged is False and board[i][
                        j].merged is False:
                        board[i + 1][j] = Tile(board[i + 1][j].number + board[i][j].number, True)
                        board[i][j] = Tile(0, False)
                        did_swap = True
    else:
        print("Invalid Input.")


def make_tiles(line):
    """Given a list of numbers, return a list of Tiles."""
    tiles = []
    for number in line:
        tiles.append(Tile(number, False))
    return tiles


if __name__ == "__main__":
    """Solve the 2048 problem."""
    board = []
    for i in range(4):
        board.append(make_tiles(list(map(int, input().split()))))
    move = int(input())
    do_move(move, board)
    display_board(board)
