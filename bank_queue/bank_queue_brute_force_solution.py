"""
Christian Felt
December 17, 2019
Solves the Kattis problem "Bank Queue"

Solution:
Compute every permutation of customers. For each permutation, for each time step i < T,
take customers' deposits in the order prescribed by the permutation, skipping customers that are no longer
waiting in line at time step i, and sum up the amount of deposits received. Return the max sum.
"""

import fileinput
from itertools import permutations

first_line = True
N = 0  # Total number of customers in line
T = 0  # Total time steps before bank closes
customers = []
for line in fileinput.input():
    tokens = line.split(" ")
    if first_line:
        N = int(tokens[0])  # Amount of deposit by customer i.
        T = int(tokens[1])  # Amount of time steps customer i will wait.
        first_line = False
    else:
        customers.append((int(tokens[0]), int(tokens[1])))

p = list(permutations(range(0,N)))

max_deposits = 0
for perm in p:
    t = 0
    this_deposits = 0
    for index in perm:
        candidate_customer = customers[index]
        if candidate_customer[1] >= t:
            this_deposits += candidate_customer[0]
            t += 1
    if this_deposits > max_deposits:
        max_deposits = this_deposits
print(max_deposits)