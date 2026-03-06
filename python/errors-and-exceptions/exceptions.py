# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Exceptions
# link: https://www.hackerrank.com/challenges/exceptions/problem

""""
Task
You are given two values a and b.
Perform integer division and print a/b.
"""

n = int(input())
for i in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError: # handling b = 0 cases
        print(f"Error Code: integer division or modulo by zero")
    except ValueError as e: # handling inputs being non-integer values 
        print(f"Error Code: {e}")