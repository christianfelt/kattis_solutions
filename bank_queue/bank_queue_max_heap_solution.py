"""
Christian Felt
December 17, 2019
Solves the Kattis problem "Bank Queue"

Solution:
Work backwards in time from T to 0. At each step t, push onto a max heap the deposit amounts of all customers who will
leave at or after time step t. This lets you know that all the customers on the heap will also be available at any previous time, i < t.
(You couldn't make an analogous assumption, working forward in time, because then some customers would leave.)
Pop the top off the max heap, representing the deposit received at time t, and add it to your running total. When you reach
t = 0, your running total will be the maximum amount of deposits it is possible to receive.
You know this greedy choice algorithm makes the correct first choice because at time T, the only deposits available
are from customers who will wait at least T time steps before leaving, so you have to choose from among them. The
same logic shows that the choices at time t = T-1, T-2, etc. work, since the heap stores all customers who are available
at each of those times, and you always choose the max deposit.
"""

import heapq
from collections import defaultdict

N, T = map(int, input().split())
deposit_max_heap = []
customers = defaultdict(list)
for i in range(N):
    c_i, t_i = map(int, input().split())
    customers[t_i].append(-c_i)  # heapq is min heap, so we make all deposit amounts negative in order to find the max.
max_deposits = 0
for t in range(T, -1, -1):
    for c in customers[t]:
        heapq.heappush(deposit_max_heap, c)
    if len(deposit_max_heap) > 0:
        max_deposits += heapq.heappop(deposit_max_heap)
print(-max_deposits)


