# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Symmetric Difference
# link: https://www.hackerrank.com/challenges/symmetric-difference/problem

""""
Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

"""

mSize = int(input())

M = set(list(map(int, input().strip().split())))

nSize = int(input())

N = set(list(map(int, input().strip().split())))

sdMN = M.difference(N) # Values in M but not in N
sdMN.update(N.difference(M)) # adding values in N but not M to the new set

sdMNlist = list(sdMN)
sdMNlist = sorted(sdMNlist) # to print in ascending order
for elem in sdMNlist:
    print(elem)

