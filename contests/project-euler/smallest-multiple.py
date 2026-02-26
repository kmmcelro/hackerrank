# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #5: Smallest Multiple
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem

""""
Task
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?
"""

#!/bin/python3

import sys
import math

def is_prime(n): # function for checking if a number is prime
    if n <= 1:
        return False
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1): 
            # any number above the square root that could be a factor would've been paired with a number less than the square root of n, so we only check up to there
            if n % i == 0:
                prime = False
                break
        return prime

def smallestMultiple(n): 
    mult = 1
    for i in range(1,n+1):
        # identify the primes so factors that already exist in other numbers [1,n] aren't counted more than necessary
        if is_prime(i): 
            # determines the highest power of the prime that exists between [1,n] and raises the prime to that power (eg [1,10] 2**3 = 8, so 10's smallest reminder would need a factor of 2**3)
            mult *= i ** int(math.log(n,i))  
    return mult
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallestMultiple(n))