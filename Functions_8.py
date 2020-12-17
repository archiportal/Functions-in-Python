import math


def fact(n):
    if (n <= 1):
        return 1

    return n * fact(n - 1)


def nPr(n, r):

    return math.floor(fact(n) /
                      fact(n - r))


n = int(input("Enter value of n:"))
r = int(input("Enter value of r:"))

print("Value of npr is:",nPr(n, r))