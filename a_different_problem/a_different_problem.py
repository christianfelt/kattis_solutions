"""
Christian Felt
January 2019
Solves the "A Different Problem" on Kattis
"""

from sys import stdin

for line in stdin:
    tokens = list(map(int, line.split()))
    print(abs(tokens[0] - tokens[1]))
