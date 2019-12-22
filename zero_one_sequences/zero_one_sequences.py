"""
Christian Felt
December 20, 2019
Solves the Kattis problem "0-1 Sequences"
"""
import time

MODULUS = 1000000007
known_chunks = {}
NUM_CHUNKS = 4


def get_num_inversions(s):
    num_inversions = 0
    num_zeros = s.count('0')
    for char in s:
        if char == '1':
            num_inversions += num_zeros
        if char == '0':
            num_zeros -= 1
    return num_inversions % MODULUS


def get_all_combs(chunk):
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
    start = time.time()
    two_k_strings = make_two_k_strings(s)
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    end = time.time()
    print("Execution time without chunks is", str(end - start))
    return total_num_inversions % MODULUS


def solve_with_chunks(s, chunk_size):  # Just for testing.
    start = time.time()
    two_k_strings = make_two_k_strings_with_chunks(s, chunk_size)
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    end = time.time()
    print("Execution time with chunks is", str(end - start))
    return total_num_inversions % MODULUS


def solve(s, chunk_size):
    if chunk_size == 1:
        two_k_strings = make_two_k_strings(s)
    else:
        two_k_strings = make_two_k_strings_with_chunks(s, chunk_size)
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    return total_num_inversions % MODULUS


def main(s):
    chunk_size = max(int(len(s) / NUM_CHUNKS), 1)
    return solve(s, chunk_size)


if __name__ == '__main__':
    s = input()
    # print(solve_with_chunks(s, 1))
    # print(solve_without_chunks(s))
    print(main(s))
