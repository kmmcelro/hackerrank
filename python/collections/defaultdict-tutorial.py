# Author: kmmcelro
# This is my solution to the Hackerrank challenge, DefaultDict Tutorial
# link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

""""
Task
The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. 
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""

from collections import defaultdict
A = defaultdict(list)
B = defaultdict(list)

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

for i in range(n): # creating the A group
    Astring = str(input())
    A[Astring].append(i+1)
    

for j in range(m): # creating B group and checking if each int is in A and what indices
    Bstring = str(input())
    bIndices = ""
    if A[Bstring]:
        for k in A[Bstring]:
            bIndices += str(k) + " "
    else:
        bIndices = "-1"
    print(bIndices)
