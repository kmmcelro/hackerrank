# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #7: 10001st prime
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

""""
Task
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the Nth prime number?
"""

#!/bin/python3

import sys

primes = [] # declaring as a global variable

def is_prime(n): # function for checking if a number is prime
    if n == 2:
        return True
    else:
        prime = True
        for i in primes: # only need to check if previous primes are factors to confirm if current number is a prime
            if n % i == 0:
                prime = False
                break
        return prime

def listofPrimes():
    count = 0
    i = 2
    while count < 10000: # appending the first 10,000 prime numbers to the list
        if is_prime(i):
            primes.append(i)
            count += 1
        i += 1
    

t = int(input().strip())
listofPrimes() # generates the list of primes in the range, so the list isn't recalculated for each test
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1]) # pulling the nth prime from list to print