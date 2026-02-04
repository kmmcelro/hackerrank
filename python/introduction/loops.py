# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Loops
# link: https://www.hackerrank.com/challenges/python-loops/problem

""""
Task
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)