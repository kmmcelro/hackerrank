# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Reduce Function
# link: https://www.hackerrank.com/challenges/reduce-function/problem

""""
Task
Given a list of rational numbers (presented as fractions), find their product, using the reduce function.
"""

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs) # since it's already converted to frac format, only product is needed for the formula
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)