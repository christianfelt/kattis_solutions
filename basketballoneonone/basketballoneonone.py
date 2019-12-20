"""
Christian Felt
December 19, 2019
Solves the 'Basketball One on One' problem on Kattis.
"""

score_log = input()
score_dict = {'A': 0, 'B': 0}
for i in range(0,len(score_log),2):
    letter = score_log[i]
    assert letter == 'A' or letter == 'B'
    score = int(score_log[i+1])
    score_dict[letter] += score
if score_dict['A'] > score_dict['B']:
    print('A')
else:
    print('B')

