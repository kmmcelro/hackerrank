# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Check Subset
# link: https://www.hackerrank.com/challenges/py-check-subset/problem

""""
Task
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

"""

def check_subset(A, B): # checks if A is a subset of B
    if A.intersection(B) == A:
        return True
    else:
        return False
    
testNum = int(input())

for i in range(0, testNum):
    ALen = int(input())
    A = set(map(int, input().strip().split()))
    BLen = int(input())
    B = set(map(int, input().strip().split()))
    print(check_subset(A, B))
