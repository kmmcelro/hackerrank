# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Tuples
# link: https://www.hackerrank.com/challenges/python-tuples/problem

""""
Task
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

This only runs in python 2 to get the accurate hash value.
"""

#if __name__ == '__main__':
#    n = int(raw_input())
#    integer_list = map(int, raw_input().split())
#    t = tuple(integer_list)
#    print(hash(t))

# Working python 3 converting list of integers to a tuple getting the hash, but only the commented out code works in hackerrank
n = int(input())
b = map(int, input().split(" "))
t = tuple(b)
print(hash(t))
