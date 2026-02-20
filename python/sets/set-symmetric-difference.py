# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Set .symmetric_difference() Operation
# link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

""""
Task
Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

"""

e = int(input())
E = set(input().split(" "))

f = int(input())
F = set(input().split(" "))

print(len(E.symmetric_difference(F)))