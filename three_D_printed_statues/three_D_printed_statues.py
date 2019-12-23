"""
Christian Felt
December 22, 2019
Solves the 3D Printed Statues problem on Kattis.
"""

statues_ordered = int(input())
production_max = 1
days_elapsed = 1
while production_max < statues_ordered:
    production_max = production_max * 2
    days_elapsed += 1
print(days_elapsed)
