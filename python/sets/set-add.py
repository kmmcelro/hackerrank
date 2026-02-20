# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Set .add()
# link: https://www.hackerrank.com/challenges/py-set-add/problem

""""
Task
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

"""

n = int(input()) 
s = set("")
for i in range(0,n):
    s.add(input())
p = len(s)
print(p)

