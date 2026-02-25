# Author: kmmcelro
# This is my solution to the Hackerrank challenge, itertools.combinations()
# link: https://www.hackerrank.com/challenges/itertools-combinations/problem

""""
Task
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

"""

from itertools import combinations

def combinateWord(string,number): # creates a list of combinations of a string with length number
    return [''.join(i) for i in combinations(string,number)]

string, number = input().split()
k = int(number)
string = sorted(string)
for i in range(1,k+1): # loops to take in account all length combinations up to length k
    comb = combinateWord(string,i)
    comb = sorted(comb)
    for singComb in comb:        
        print(singComb)
