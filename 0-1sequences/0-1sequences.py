"""
Christian Felt
December 20, 2019
Solves the Kattis problem "0-1 Sequences"
"""

from itertools import permutations


def index_of_rightmost_one(s, j):  # Get index of rightmost one in the string s in the range [0,j]
    for i in range(j, -1, -1):
        if int(s[i]) == 1:
            return i
    return -1


def get_num_inversions(s):
    # Gets the number of inversions of a given string in which all ? have been replaced by 0 or 1.
    # At first we can't assume the rightmost digit is 1, so there are two cases.
    n = len(s) - 1
    j = index_of_rightmost_one(s, n)
    num_inversions = 0
    if j == -1:
        return 0
    # Case 1: rightmost digit is 0
    if s[n] == str(0):
        num_inversions = n - j
        j -= 1
    else:  # Case 2: rightmost digit is 1
        if n - j == 0 or n - j == 1:
            num_inversions += 0
        elif n - j > 1:
            num_inversions += n - j - 1
        else:
            raise Exception("n - j is invalid value.")
        j -= 1
    while j > 0:  # Now we can assume the rightmost digit is 1.
        j = index_of_rightmost_one(s, j)
        if j == -1:
            break
        if n - j == 0 or n - j == 1:
            num_inversions += 0
        elif n - j > 1:
            num_inversions += n - j - 1
        else:
            raise Exception("n - j is invalid value.")
        n -= 1
        j -= 1
    return num_inversions


def make_two_k_strings(s):
    two_k_strings = []
    k = s.count('?')
    for i in range(2**k):
        this_perm = bin(i)[2:].zfill(k)  # Strip 0b prefix off binary number.
        this_s = s
        for j in range(k):
            this_s = this_s.replace('?', this_perm[j], 1)
        two_k_strings.append(this_s)
    return two_k_strings

s = input()
two_k_strings = make_two_k_strings(s)  # Here go all possible replacements of ? in s by 0 or 1
total_num_inversions = 0
for st in two_k_strings:
    total_num_inversions += get_num_inversions(st)
print(total_num_inversions)
