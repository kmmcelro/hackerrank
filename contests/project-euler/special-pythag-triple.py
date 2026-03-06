# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #9: Special Pythagorean Triplet
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

""""
Task
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
                    a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2

Given N, Check if there exists any Pythagorean triplet for which a + b + c = N
Find maximum possible value of abc among all such Pythagorean triplets, If there is no such Pythagorean triplet print -1.
"""

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    maxProd = -1 # default if no triplets
    
    for a in range(1, n//2): # ensures all triplets are checked
        b = (n*n - 2*a*n) / (2*(n-a))
        if b.is_integer() is False: # next a if b isn't an int
            continue 
        c = (b*b + a*a)**(1/2)
        if c.is_integer() is False: # next a if c isn't an int
            continue
        product = a*b*c # finding the product of current triple
        if product > maxProd: # checking against current max and changing the max if it's higher
            maxProd = product
    print(int(maxProd))