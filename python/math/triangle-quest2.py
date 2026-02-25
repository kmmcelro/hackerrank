# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Triangle Quest 2
# link: https://www.hackerrank.com/challenges/triangle-quest-2/problem

""""
Task
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

"""

for i in range(1,int(input())+1): 
     print(((10**i - 1)//9)**2)