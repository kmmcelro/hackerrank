# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Check Strict Superset
# link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

""""
Task
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

"""

def check_strict_superset(A, B):
    if A.intersection(B) == B:
        return A.difference(B) is not None
    else:
        return False


A = set(map(int, input().strip().split()))
testNum = int(input())

result = True

for i in range(0, testNum):
    B = set(map(int, input().strip().split()))
    if check_strict_superset(A, B) is not True: # If it is not true in at least one case it's false
        result = False
        
print(result)
