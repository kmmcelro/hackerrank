# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #3: Largest Prime Factor
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

""""
Task
First line contains T, the number of test cases. This is followed by T lines each containing an integer N.
What is the largest prime factor of a given number N?
"""


#!/bin/python3

import sys
    
def maxprimefactor(n):
    # defaults to 1 since it's always a factor
    maxfactor = 1
    while n % 2 == 0: # Checks if it is even and changes max to 2 if it is
        maxfactor = 2
        n //= 2
    i = 3
    while i * i <= n: # Checks the odd numbers in the same way as 2 was just checked and replaces maxfactor each time a prime factor is found, since i either increases or stays equal each subsequent loop
        while n % i == 0:
            maxfactor = i
            n //= i
        i += 2
    if n > maxfactor: # if the number left after those factors were taken out is higher than the current max, it's a factor and it's prime, so it's the new max
        maxfactor = n
    return maxfactor


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    factor = maxprimefactor(n)
    print(factor)
