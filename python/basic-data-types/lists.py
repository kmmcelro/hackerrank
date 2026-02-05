# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Lists
# link: https://www.hackerrank.com/challenges/python-lists/problem

""""
Task
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""


def pickfunct(L, cmd):
    action = cmd[0] # first value is what action is happening to the list
    if (action == 'insert'):
        ind = int(cmd[1])
        num = int(cmd[2])
        L.insert(ind,num)
    elif (action == 'print'):
        print(L)
    elif (action == 'remove'):
        num = int(cmd[1])
        L.remove(num)
    elif (action == 'append'):
        num = int(cmd[1])
        L.append(num)
    elif (action == 'sort'):
        L.sort()
    elif (action == 'pop'):
        L.pop()
    elif(action == 'reverse'):
        L.reverse()
    return L

if __name__ == '__main__':
    N = int(input())
    L = []
    for n in range(0,N): # cycles through the actions
        cmd = input().split(" ")
        L = pickfunct(L,cmd)