# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Print Function
# link: https://www.hackerrank.com/challenges/python-print/problem

""""
Task
Print the list of integers from 1 through n as a string, without spaces.
"""

def printingN(N):
    for i in range(1,N+1): 
        print(i, end='')
        
n = int(input())
printingN(n)