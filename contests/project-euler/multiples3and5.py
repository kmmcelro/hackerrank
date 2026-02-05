# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #1: Multiples of 3 and 5
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

""""
Task
Find the sum of all the multiples of 3 or 5 below N.
"""

#!/bin/python3

import sys

def seriessum(nminus, x): # finds the sum of a series that starts with x and increases by x amount, but all series values are less than or equal to nminus
    a = nminus // x
    asum = a * x * (a + 1) // 2
    return asum


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # since 15 is a multiple of both 3 and 5, the sum of all multiple of 15 need to be subtracted to undo the double counting
    nsum = seriessum(n-1, 3) + seriessum(n-1, 5) - seriessum(n-1, 15)
    print(nsum)
    
