# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Collections.deque()
# link: https://www.hackerrank.com/challenges/py-collections-deque/problem

""""
Task
Perform append, pop, popleft and appendleft methods on an empty deque d.

"""

from collections import deque

d = deque()

numSteps = int(input())

for i in range(numSteps): # executing the command inputs
    step = list(map(str,input().strip().split()))
    if step[0] == 'append':
        d.append(step[1])
    elif step[0] == 'appendleft':
        d.appendleft(step[1])
    elif step[0] == 'pop':
        d.pop()
    elif step[0] == 'popleft':
        d.popleft()
    else:
        print("Not one of the requested commands")

string = ""

for elem in d: # creating a string to list queue elements in order                   
     string += elem.upper() + " "

print(string)
