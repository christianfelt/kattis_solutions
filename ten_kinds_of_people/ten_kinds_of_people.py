"""
Christian Felt
December 2019
Solves the 10 Kinds of People problem on Kattis
"""
import copy

my_map = {0: "binary", 1: "decimal"}


def fill(r0, c0, board, filler_char):
    """Fill all adjacent squares of the same type as where we start with filler_char."""
    filled_char = board[r0][c0]
    fill_helper(r0, c0, board, filler_char, filled_char)


def fill_helper(r0, c0, board, filler_char, filled_char):
    """Recursively fill all adjacent squares of type filled_char with filler_char."""
    if board[r0][c0] == filled_char:
        board[r0][c0] = filler_char
        if r0 + 1 < len(board):
            fill_helper(r0 + 1, c0, board, filler_char, filled_char)
        if r0 - 1 > -1:
            fill_helper(r0 - 1, c0, board, filler_char, filled_char)
        if c0 + 1 < len(board[0]):
            fill_helper(r0, c0 + 1, board, filler_char, filled_char)
        if c0 - 1 > -1:
            fill_helper(r0, c0 - 1, board, filler_char, filled_char)
    else:
        return


def query_board(r1, c1, r2, c2, board):
    """Check if fill starting from point 1 reaches point 2, and return yes or no in the form required by the problem,
    according to what kind of square we started on."""
    starting_char = board[r1][c1]
    board_copy = copy.deepcopy(board)
    fill(r1, c1, board_copy, 4)
    if board_copy[r1][c1] == board_copy[r2][c2]:
        return my_map[starting_char]
    else:
        return "neither"


def main():
    """Process inputs and solve the Ten Kinds of People problem on Kattis."""
    r, c = map(int, input().split())
    board = []
    for i in range(r):
        board.append(list(map(int, list(input()))))
    n = int(input())
    for i in range(n):
        r1, c1, r2, c2 = map(int, input().split())
        print(query_board(r1 - 1, c1 - 1, r2 - 1, c2 - 1, board))  # Problem indexes from 1, I index from 0.


if __name__ == '__main__':
    main()
