"""
Christian Felt
December 20, 2019
Solves the Kattis problem "0-1 Sequences"
"""

# TODO: Use Dynamic Programming more extensively
# TODO: Find some way to do without make_two_k_strings or make it faster

MODULUS = 1000000007
known_sols = {}
known_chunks = {}
CHUNK_SIZE = 4


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


def make_two_k_strings_with_chunking(s):
    two_k_strings = set()
    remainder = s[len(s) - (len(s) % CHUNK_SIZE):]
    for i in range(0, len(s) - CHUNK_SIZE + 1, CHUNK_SIZE):
        chunk = s[i:i+CHUNK_SIZE]
        if chunk not in known_chunks:
            print("here")
            current_chunks = []
            k = chunk.count('?')
            for q in range(2 ** k):
                this_perm = bin(q)[2:].zfill(k)  # Strip 0b prefix off binary number.
                this_chunk = chunk
                for j in range(k):
                    this_chunk = this_chunk.replace('?', this_perm[j], 1)
                current_chunks.append(this_chunk)
            known_chunks[chunk] = current_chunks
        if len(two_k_strings) == 0:
            for element in known_chunks[chunk]:
                two_k_strings.add(element)
        else:
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
    if remainder not in known_chunks:
        k = remainder.count('?')
        remainder_chunks = []
        for q in range(2 ** k):
            this_perm = bin(q)[2:].zfill(k)  # Strip 0b prefix off binary number.
            this_chunk = remainder
            for j in range(k):
                this_chunk = this_chunk.replace('?', this_perm[j], 1)
            remainder_chunks.append(this_chunk)
        known_chunks[remainder] = remainder_chunks
    strings_to_remove = set()
    strings_to_add = set()
    for stub_string in two_k_strings:
        for element in known_chunks[remainder]:
            strings_to_add.add(stub_string + element)
        strings_to_remove.add(stub_string)
    for string_to_remove in strings_to_remove:
        two_k_strings.remove(string_to_remove)
    for string_to_add in strings_to_add:
        two_k_strings.add(string_to_add)
    return two_k_strings


def main(s):
    if len(s) >= CHUNK_SIZE:
        two_k_strings = make_two_k_strings_with_chunking(s)  # Here go all possible replacements of ? in s by 0 or 1
    else:
        two_k_strings = make_two_k_strings(s)
    # two_k_strings = make_two_k_strings(s)
    total_num_inversions = 0
    for st in two_k_strings:
        total_num_inversions += get_num_inversions(st)
    return total_num_inversions % MODULUS


if __name__ == '__main__':
    s = input()
    print(main(s))
