# Author: kmmcelro
# This is my solution to the Hackerrank challenge, itertools.permutations()
# link: https://www.hackerrank.com/challenges/itertools-permutations/problem

""""
Task
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

"""

from itertools import permutations

def permuteWord(string,number): # creates a list of permutations of a string with length number
    return [''.join(i) for i in permutations(string,number)]

string, number = input().split()

permute = permuteWord(string,int(number))
permute = sorted(permute) # to sort into lexicographic order

for singpermute in permute:
    print(singpermute)
