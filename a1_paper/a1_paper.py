"""
Christian Felt
December 2019
Solves the A1 Paper problem on Kattis
"""
A1_WIDTH = 1 / (2 ** (3 / 4))
A1_LENGTH = 2 / (2 ** (5 / 4))

A2_WIDTH = 1 / (2 ** (5 / 4))
A2_LENGTH = 1 / (2 ** (3 / 4))


class Sheet:
    """Represent the sheet of paper that is being taped together in this problem."""

    def __init__(self, length, width, amt_tape, sheets, max_sheet_index, current_index):
        self.length = length
        self.width = width
        self.amt_tape = amt_tape
        self.sheets = sheets  # List of all sheets not yet used.
        self.max_sheet_index = max_sheet_index
        self.current_index = current_index

    def add_next_largest_sheet(self):
        """Add the largest remaining sheet of paper to the total."""
        for i in range(self.max_sheet_index - 1):
            if i > self.current_index:
                old_length = self.length
                self.length = self.width
                self.width = old_length / 2
                self.current_index += 1
            if self.sheets[i] > 0:
                self.sheets[i] -= 1
                if self.amt_tape == -1:  # No tape is needed for first sheet of paper, but change -1
                    # to 0 so that we can accumulate tape next time.
                    self.amt_tape = 0
                else:
                    self.amt_tape += self.length
                return self.width * self.length
        return "impossible"


if __name__ == "__main__":
    max_sheet_index = int(input())  # Index of smallest paper size, A_max_sheet_index
    sheets = list(map(int, input().split()))
    current_area = 0.0
    amt_tape = -1  # Arbitrary impossible value to show no tape has been added yet.
    current_index = 0
    This_Sheet = Sheet(A2_LENGTH, A2_WIDTH, amt_tape, sheets, max_sheet_index, current_index)
    while current_area < A1_WIDTH * A1_LENGTH:
        this_area = This_Sheet.add_next_largest_sheet()
        if this_area == "impossible":
            This_Sheet.amt_tape = "impossible"
            break
        else:
            current_area += this_area
    print(This_Sheet.amt_tape)
