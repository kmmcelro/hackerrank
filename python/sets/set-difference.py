# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Set .difference() Operation
# link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

""""
Task
Students of District College have a subscription to English and French newspapers. 
Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to only English newspapers.

"""

e = int(input())
E = set(input().split(" "))

f = int(input())
F = set(input().split(" "))
print(len(E.difference(F)))