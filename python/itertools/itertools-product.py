# Author: kmmcelro
# This is my solution to the Hackerrank challenge, itertools.product()
# link: https://www.hackerrank.com/challenges/itertools-product/problem

""""
Task
You are given a two lists A and B. Your task is to compute their cartesian product A X B.

"""

from itertools import product

A = list(map(int, input().rstrip().split())) 
B = list(map(int, input().rstrip().split())) 

AXB = list(product(A,B))
axb = ''
for tup in AXB:
    axb += str(tup) + " "
print(axb)
