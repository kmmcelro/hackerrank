# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #8: Largest product in a series
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem

""""
Task
Find the greatest product of K consecutive digits in the N digit number.
"""

#!/bin/python3

import sys

from math import prod 

def consecutiveProduct(numString, n, k):
    maxProd = 0
    for i in range(0, n-k):
        product = prod(map(int, list(numString[i:i+k]))) # finding the product from this section of numbers
        if product > maxProd: #checking against current max
            maxProd = product
    return maxProd

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(consecutiveProduct(num, n, k))