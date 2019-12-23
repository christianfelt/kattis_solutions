"""
Christian Felt
December 20, 2019
Solves the Kattis problem "0-1 Sequences"

Solution idea: To get minimum number of inversions in a string of 0s and 1s
to sort the string in non-decreasing order, for each 1 simply add the number of
zeros to the right, and for each 0 decrease the number of zeros. Imagine that you are
scooting beads (the 1s) down to the right of a string, where the zeros are empty space.
To convert ?s into 0s or 1s, take all possible combinations, but use dynamic programming to
remember the ones you have already computed, in smallish chunks, storing a dictionary with entries like
'??': '00, 01, 10, 11'.
"""

import time

MODULUS = 1000000007
known_chunks = {}
NUM_CHUNKS = 4


def get_num_inversions(s):
    """Given a string with only 0s and 1s, calculate minimum number of inversions to sort in non-descending order."""
    num_inversions = 0
    num_zeros = s.count('0')
    for char in s:
        if char == '1':
            num_inversions += num_zeros
        if char == '0':
            num_zeros -= 1
    return num_inversions % MODULUS


def get_all_combs(chunk):
    """Given a string of 0s, 1s, and ?s, return all ways of replacing ? with 0 or 1."""
    current_chunks = []
    k = chunk.count('?')
    for q in range(2 ** k):
        this_perm = bin(q)[2:].zfill(k)  # Strip 0b prefix off binary number.
        this_chunk = chunk
        for j in range(k):
            this_chunk = this_chunk.replace('?', this_perm[j], 1)
        current_chunks.append(this_chunk)
    return current_chunks


def add_new_combs_to_k_strings(two_k_strings, chunk):
    """Given list of strings of 0s and 1s, concatenate each of these to each of the existing, growing
    strings in two_k_strings and delete the previous contents of two_k_strings."""
    strings_to_remove = set()
    strings_to_add = set()
    for stub_string in two_k_strings:
        for element in known_chunks[chunk]:
            strings_to_add.add(stub_string + element)
        strings_to_remove.add(stub_string)
    for string_to_remove in strings_to_remove:
        two_k_strings.remove(string_to_remove)
    for string_to_add in strings_to_add:
        two_k_strings.add(string_to_add)


def make_two_k_strings(s):
    """Find all instantiations in 0s and 1s of the string given in 0s, 1s, and ?s."""
    two_k_strings = set()
    k = s.count('?')
    for i in range(2 ** k):
        this_perm = bin(i)[2:].zfill(k)  # Strip 0b prefix off binary number.
        this_s = s
        for j in range(k):
            this_s = this_s.replace('?', this_perm[j], 1)
        two_k_strings.add(this_s)
    return two_k_strings


def make_two_k_strings_with_chunks(s, chunk_size):
    """Find all instantiations in 0s and 1s of the string given in 0s, 1s, and ?s, using dynamic programming
    to process the given string in chunks and store intermediate results."""
    two_k_strings = set()
    remainder = s[len(s) - (len(s) % chunk_size):]
    for i in range(0, len(s) - chunk_size + 1, chunk_size):
        chunk = s[i:i + chunk_size]
        if chunk not in known_chunks:
            current_chunks = get_all_combs(chunk)
            known_chunks[chunk] = current_chunks
        if len(two_k_strings) == 0:
            for element in known_chunks[chunk]:
                two_k_strings.add(element)
        else:
            add_new_combs_to_k_strings(two_k_strings, chunk)
    if remainder not in known_chunks:
        remainder_chunks = get_all_combs(remainder)
        known_chunks[remainder] = remainder_chunks
    add_new_combs_to_k_strings(two_k_strings, remainder)
    return two_k_strings


def solve_without_chunks(s):  # Just for testing.
    """Times the solution without chunks."""
    start = time.time()
    two_k_strings = make_two_k_strings(s)
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    end = time.time()
    print("Execution time without chunks is", str(end - start))
    return total_num_inversions % MODULUS


def solve_with_chunks(s, chunk_size):  # Just for testing.
    """Times the solution with chunks."""
    start = time.time()
    two_k_strings = make_two_k_strings_with_chunks(s, chunk_size)
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    end = time.time()
    print("Execution time with chunks is", str(end - start))
    return total_num_inversions % MODULUS


def solve(s, chunk_size):
    """Solves the problem with chunks if possible."""
    if chunk_size == 1:
        two_k_strings = make_two_k_strings(s)
    else:
        two_k_strings = make_two_k_strings_with_chunks(s, chunk_size)
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    return total_num_inversions % MODULUS


def main(s):
    """Solves the zero one sequences problem on Kattis."""
    chunk_size = max(int(len(s) / NUM_CHUNKS), 1)
    return solve(s, chunk_size)


if __name__ == '__main__':
    s = input()
    # print(solve_with_chunks(s, 1))
    # print(solve_without_chunks(s))
    print(main(s))
