# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #6: Sum square difference
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem

""""
Task
The sum of the squares of the first ten natural numbers is, 1**2 + 2**2 + ... + 10**2 = 385. The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)**2 = 55**2 = 3085. 
Hence the absolute difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.
"""

#!/bin/python3

import sys

def sumSqDiff(n):
    sqSum = ((1+n)*n/2)**2 # finding the square of the sum of the sequence 
    sumSq = 0
    for i in range(1, n+1): # finding the sum of the squence of squares
        sumSq += i**2
    return int(sqSum - sumSq)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumSqDiff(n))