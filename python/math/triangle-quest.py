# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Triangle Quest
# link: https://www.hackerrank.com/challenges/python-quest-1/problem

""""
Task
You are given a positive integer N.
Print a numerical triangle of height N-1.
Use no more than two lines. The first line (the for statement) is already written for you. 
You have to complete the print statement.

"""

for i in range(1,int(input())): 
    print((10**i//9)*i)