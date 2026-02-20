# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Set .intersection() Operation
# link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

""""
Task
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.

"""

n = int(input())
N = set(input().split(" "))

b = int(input())
B = set(input().split(" "))
print(len(N.intersection(B)))