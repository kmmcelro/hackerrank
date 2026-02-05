# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Nested Lists
# link: https://www.hackerrank.com/challenges/nested-list/problem

""""
Task
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

def check(L):
    L.sort(key=lambda x: (x[1], x[0])) # sort by scores then names
    G = L[0][1] # lowest score in the list
    Gp = L[len(L)-1][1] # highest score in the list
    for n in range(1,len(L)): # skips lowest score and cycles through whole list
        y = L[n][1]
        if ((y > G) and (y <= Gp)):
            # first value above G is the second lowest, so I fixed Gp to that so we don't print people with grades above this value now that we have it
            Gp = y 
            print(L[n][0])

if __name__ == '__main__':
    y = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st = [name,score]
        y.append(st)
        
    check(y)