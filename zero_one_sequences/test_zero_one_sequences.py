import unittest
from zero_one_sequences import main, solve_with_chunks, solve_without_chunks


class MyTestCase(unittest.TestCase):
    def test_three_digits(self):
        self.assertEqual(main("100"), 2)
        self.assertEqual(main("010"), 1)
        self.assertEqual(main("001"), 0)
        self.assertEqual(main("000"), 0)
        self.assertEqual(main("?0?"), 3)
        self.assertEqual(main("?00"), 2)
        self.assertEqual(main("???"), 6)

    def test_four_digits(self):
        self.assertEqual(main("????"), 24)

    def test_five_digits(self):
        self.assertEqual(main("11110"), 4)
        self.assertEqual(main("11111"), 0)
        self.assertEqual(main("11100"), 6)
        self.assertEqual(main("11000"), 6)
        self.assertEqual(main("10100"), 5)
        self.assertEqual(main("10000"), 4)
        self.assertEqual(main("?000?"), 7)

    def test_six_digits(self):
        self.assertEqual(main("100101"), 4)

    def test_chunking(self):
        self.assertEqual(solve_with_chunks("?????", 4), solve_without_chunks("?????"))

    def test_large_chunking(self):
        self.assertEqual(main("????????????????????"), 49807360)


if __name__ == '__main__':
    unittest.main()
