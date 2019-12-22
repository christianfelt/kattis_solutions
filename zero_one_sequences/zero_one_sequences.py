"""
Christian Felt
December 20, 2019
Solves the Kattis problem "0-1 Sequences"
"""

# TODO: Use Dynamic Programming more extensively
# TODO: Find some way to do without make_two_k_strings or make it faster

MODULUS = 1000000007
known_sols = {}


def get_num_inversions(s):
    if s in known_sols:
        return known_sols[s]
    else:
        num_inversions = 0
        num_zeros = s.count('0')
        for char in s:
            if char == '1':
                num_inversions += num_zeros
            if char == '0':
                num_zeros -= 1
        this_sol = num_inversions % MODULUS
        known_sols[s] = this_sol
        return this_sol


def make_two_k_strings(s):
    two_k_strings = []
    k = s.count('?')
    for i in range(2 ** k):
        this_perm = bin(i)[2:].zfill(k)  # Strip 0b prefix off binary number.
        this_s = s
        for j in range(k):
            this_s = this_s.replace('?', this_perm[j], 1)
        two_k_strings.append(this_s)
    return two_k_strings


def main(s):
    two_k_strings = make_two_k_strings(s)  # Here go all possible replacements of ? in s by 0 or 1
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    return total_num_inversions % MODULUS


if __name__ == '__main__':
    s = input()
    print(main(s))
