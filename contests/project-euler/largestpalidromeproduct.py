# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #4: Largest Palidrome Product
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem

""""
Task
A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is 101101 = 143 x 707.

Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
"""


#!/bin/python3

import sys
import math

def is_palidrome(nstr): # check for palidromes
    m = len(nstr)// 2
    l = len(nstr) - 1
    for i in range(0, m):
        if nstr[i] != nstr[l-i]:
            return False
    return True

def threedigitfactors(n):
    i = 102  # smallest value that when divided into 101101 the smallest palidrome gets a dividend under 1000
    while i * i <= n: # when looking for factors in pairs you won't find any new pairs after sq of n and sq of n is bound to be either equal or less than 999
        if n % i == 0: 
            if 100 < n // i < 999: # making sure the other factor is 3 digits
                return True
        i += 1
    return False

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    nmax = 999*999 # any palidromes above this can't be a product of two 3-digit numbers
    if n > nmax:
        n = nmax
    while is_palidrome(list(str(n))) is False or threedigitfactors(n) is False: 
        n = n-1
    print(n)