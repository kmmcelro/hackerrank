# Author: kmmcelro
# This is my solution to the Hackerrank challenge, itertools.combinations_with_replacement()
# link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

""""
Task
You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
"""

from itertools import combinations_with_replacement

def combinatewrWord(string,number): # creates a list of combinations with replacement of a string with length number
    return [''.join(i) for i in combinations_with_replacement(string,number)]

string, number = input().split()
k = int(number)
string = sorted(string)
comb = combinatewrWord(string,k)
comb = sorted(comb)
for singComb in comb:        
    print(singComb)