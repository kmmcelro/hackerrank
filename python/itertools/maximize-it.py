# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Maximize It!
# link: https://www.hackerrank.com/challenges/maximize-it/problem

""""
Task
You are given a function f(X) = X**2. You are also given K lists. The ith list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:

S = (f(X1) + f(X2) + ... + f(Xk)) % M

Xi denotes the element picked from the ith list. Find the maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. 
The maximum value that you can obtain, will be the answer to the problem.
"""

import itertools as it

k, m = map(int,input().split(" "))

nlist = []

for i in range(0, k): # creating the list of lists
    n = list(map(int,input().split(" ")))
    nlist.append(n[1:])
combolist = list(it.product(*nlist)) # list of all potential combinations of elements
nmax = 0
for ncombo in combolist: # finds the combination with the max value for the formula
    x = sum(map(pow, ncombo, it.repeat(2, k))) % m
    if x > nmax:
        nmax = x
print(nmax)