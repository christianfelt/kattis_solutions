"""
Christian Felt
January 2020
Solves the "Above Average" problem on Kattis.
"""
from sys import stdin

input_string = stdin.read()
tokens = list(map(int, input_string.split()))
c = tokens[0]
j = 1
for i in range(c):
    grade_list = []
    running_total = 0.0
    n = tokens[j]
    k = j
    while j < k + n:
        j += 1
        this_grade = tokens[j]
        grade_list.append(this_grade)
        running_total += this_grade
    average_grade = running_total / n
    j += 1
    num_above_avg = 0.0
    for grade in grade_list:
        if grade > average_grade:
            num_above_avg += 1
    result = 100 * (num_above_avg / n)
    print("%.3f" % result + "%")
