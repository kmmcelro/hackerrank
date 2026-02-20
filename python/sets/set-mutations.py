# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Set Mutations
# link: https://www.hackerrank.com/challenges/py-set-mutations/problem

""""
Task
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

"""

lenA = int(input())

A = set(map(int, input().strip().split()))
numSets = int(input())

for i in range(0, numSets):
    command, lenSet = input().strip().split()
    bSet =  set(map(int, input().strip().split()))
    run = getattr(A, command)
    run(bSet)


print(sum(A))