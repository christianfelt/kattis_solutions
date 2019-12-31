"""
Christian Felt
December 2019
Solves the "Aaah!" problem on Kattis
"""
doctor = input()
jon = input()
if doctor.count("a") >= jon.count("a"):
    print("go")
else:
    print("no")
