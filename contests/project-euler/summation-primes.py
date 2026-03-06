# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #9: Summation of primes
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

""""
Task
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes not greater than given N.
"""

#!/bin/python3

import sys

N = 1000000

primeSieve = [True] * (N+1)
primeSieve[0] = primeSieve[1] = False
primeSum = [0] * (N+1)

for i in range(2, int(N**.5) + 1): # saving whether or not a number is prime for easy look up
    if primeSieve[i]:
        for j in range(i*i, N+1, i):
            primeSieve[j] = False
            

for i in range(2, N+1): # saving cummulative sum of prime numbers up to and including the index (if it's a prime)
    if primeSieve[i]:
        primeSum[i] = i + primeSum[i-1]
    else:
        primeSum[i] = primeSum[i-1]


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primeSum[n])