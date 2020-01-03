"""
Christian Felt
January 2020
Solves the "Abstract Painting" problem on Kattis.
"""

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


# def valid_add(grid, square, row, col):
#     if len(grid[row]) == 0 and row == 0 and col == 0:
#         grid[row].append(square)
#         return 1
#     else:
#         grid[row].append(square)
#         assert grid[row][col] == square
#         is_valid = True
#         if len(grid) > row + 1 and len(grid[row + 1]) > col:  # Check below
#             this_square = grid[row + 1][col]
#             if this_square.top_edge != square.bottom_edge:
#                 is_valid = False
#         if row > 0 and is_valid:
#             this_square = grid[row - 1][col]  # Check above
#             if this_square.bottom_edge != square.top_edge:
#                 is_valid = False
#         if col > 0 and is_valid:  # Check left
#             this_square = grid[row][col - 1]
#             if this_square.right_edge != square.left_edge:
#                 is_valid = False
#         if not is_valid:
#             grid[row].pop()
#             return 0
#         else:
#             return 1

def brute_force(R, C):
    """Make all possible paintings then count which ones are good."""
    paintings = []
    for q in range(R * C * 18):
        paintings.append([])
        for i in range(R):
            paintings[q].append([])
            for j in range(C):
                for valid_square in VALID_SQUARES:
                    paintings[q][i].append(valid_square)
    num_good_paintings = 0
    for painting in paintings:
        if is_valid_painting(painting, R, C):
            num_good_paintings += 1
    return num_good_paintings


# def one_by_two():
#     good_paintings = []
#
#     for valid_square1 in VALID_SQUARES:
#         painting = []
#         valid_add(painting, valid_square1, 0, 0)
#         for valid_square2 in VALID_SQUARES:
#             valid_add(painting, valid_square2, 0, 1)
#
#     grid = [[]]
#     valid_add(grid, VALID_SQUARES[0], 0, 0)
#     valid_add(grid, VALID_SQUARES[0], 0, 1)
#     print(grid)
#     # for valid_square in VALID_SQUARES:
#     #     valid_add(grid, valid_square,0,0)
#
#
# one_by_two()

# def brute_force(R, C):
#     good_paintings = set()
#     dead_ends = set()
#     num_good_paintings = 0
#     grids = []
#     for i in range(R):
#         grids.append([])
#         for j in range(C):
#             for valid_square in VALID_SQUARES:
#                 if is_valid_add(grid, valid_square):
#                     grid[i].append(valid_square)
#                     break


# pass
#  Make square
#  Add square to grid
#  Check whether all requirements are met
#  If yes, keep going
#  If no, add current grid to list of invalid beginnings.

T = int(input())
for i in range(T):
    R, C = list(map(int, input().split()))
    print(brute_force(R, C))
