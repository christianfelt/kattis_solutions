"""
Christian Felt
January 2020
Solves the "Abstract Painting" problem on Kattis.
"""
from itertools import combinations_with_replacement, permutations

COLORS = {"red", "green", "blue"}


class Square:
    def __init__(self, left_edge, top_edge, right_edge, bottom_edge):
        self.left_edge = left_edge
        self.top_edge = top_edge
        self.right_edge = right_edge
        self.bottom_edge = bottom_edge

    def display(self):
        print(self.top_edge + "_")
        print("|" + self.left_edge + " " + self.right_edge + "|")
        print(self.bottom_edge + "_")

    def __eq__(self, other):
        return self.bottom_edge == other.bottom_edge and self.top_edge == other.top_edge \
               and self.left_edge == other.left_edge and self.right_edge == other.right_edge


VALID_SQUARES = []
for color1 in COLORS:
    for color2 in COLORS:
        if color1 != color2:
            VALID_SQUARES.append(Square(color1, color1, color2, color2))
            VALID_SQUARES.append(Square(color2, color1, color1, color2))
            VALID_SQUARES.append(Square(color1, color2, color1, color2))


def make_paintings(R, C):
    square_indices = range(0, len(VALID_SQUARES))
    c = combinations_with_replacement(square_indices, R * C)
    perms = []
    for comb in c:
        perms.extend(list(permutations(comb)))
    perms = set(perms)  # Get rid of duplicates.
    perms_grids = []
    for q, p in enumerate(perms):
        k = 0
        perms_grids.append([])
        for i in range(R):
            perms_grids[q].append([])
            for j in range(C):
                perms_grids[q][i].append(VALID_SQUARES[p[k]])
                k += 1
    return perms_grids


def is_valid_painting(grid, R, C):
    for i in range(R):
        for j in range(C):
            this_square = grid[i][j]
            if i < R - 1:  # Check below
                other_square = grid[i + 1][j]
                if this_square.bottom_edge != other_square.top_edge:
                    return False
            if i > 0:  # Check above
                other_square = grid[i - 1][j]
                if this_square.top_edge != other_square.bottom_edge:
                    return False
            if j < C - 1:  # Check right
                other_square = grid[i][j + 1]
                if this_square.right_edge != other_square.left_edge:
                    return False
            if j > 0:  # Check left
                other_square = grid[i][j - 1]
                if this_square.left_edge != other_square.right_edge:
                    return False

    return True


def brute_force(R, C):
    """Make all possible paintings then count which ones are good."""
    paintings = make_paintings(R, C)
    num_good_paintings = 0
    for painting in paintings:
        if is_valid_painting(painting, R, C):
            num_good_paintings += 1
    return num_good_paintings


T = int(input())
for i in range(T):
    R, C = list(map(int, input().split()))
    print(brute_force(R, C))
