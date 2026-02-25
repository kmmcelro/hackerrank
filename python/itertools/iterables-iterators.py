# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Iterables and Iterators
# link: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

""""
Task
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""

import itertools
N = int(input())

nlist = input().split(" ")

K = int(input())
total = 0
count = 0
for n in itertools.combinations(nlist, K): # loop to count all k length combinations and all combinations that contain k
    total += 1
    if 'a' in n:
        count += 1
print(count/total)