import unittest
from ten_kinds_of_people import fill, query_board


class TenKindsOfPeopleTests(unittest.TestCase):
    def test_fill1(self):
        board = [[1, 1, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 0, 0]]

        filled_board = [[1, 1, 1, 4],
                        [1, 4, 1, 4],
                        [1, 4, 1, 4],
                        [1, 4, 1, 4],
                        [1, 4, 4, 4]]

        fill(0, 3, board, 4)
        self.assertEqual(board, filled_board)

    def test_fill2(self):
        board = [[1, 1, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 0, 0]]

        filled_board = [[6, 6, 6, 0],
                        [6, 0, 6, 0],
                        [6, 0, 6, 0],
                        [6, 0, 6, 0],
                        [6, 0, 0, 0]]

        fill(2, 0, board, 6)
        self.assertEqual(board, filled_board)

    def test_query_board(self):
        board = [[1, 1, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 1, 0],
                 [1, 0, 0, 0]]
        r1 = 1
        c1 = 1
        r2 = 0
        c2 = 3
        self.assertEqual(query_board(r1, c1, r2, c2, board), "binary")

    def test_query_board(self):
        board = [[1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1]]
        r1 = 0
        c1 = 0
        r2 = 6
        c2 = 0
        self.assertEqual(query_board(r1, c1, r2, c2, board), "decimal")

        r1 = 1
        c1 = 0
        r2 = 5
        c2 = 0
        self.assertEqual(query_board(r1, c1, r2, c2, board), "neither")

    def test_query_board2(self):
        board = [[1, 0, 1, 0],
                 [0, 1, 0, 1],
                 [1, 0, 1, 0]]
        r1 = 0
        c1 = 2
        r2 = 1
        c2 = 3
        self.assertEqual(query_board(r1, c1, r2, c2, board), "neither")

        r1 = 2
        c1 = 3
        r2 = 0
        c2 = 1
        self.assertEqual(query_board(r1, c1, r2, c2, board), "neither")


if __name__ == '__main__':
    unittest.main()
