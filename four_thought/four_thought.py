"""
Christian Felt
December 2019
Solves the Kattis problem "4 Thought"
"""

OPS = {"+", "-", "*", "/"}


def solve(n):
    for op0 in OPS:
        for op1 in OPS:
            for op2 in OPS:
                this_sol_str = "4 " + op0 + " 4 " + op1 + " 4 " + op2 + " 4"
                if eval(this_sol_str) == n:
                    return this_sol_str + " = " + str(n)
    return "no solution"


def main():
    m = int(input())
    for i in range(m):
        print(solve(int(input().strip())))


if __name__ == "__main__":
    main()
