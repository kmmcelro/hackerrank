# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Zipped!
# link: https://www.hackerrank.com/challenges/zipped/problem

""""
Task
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

Average score = (Sum of scores obtained in all subjects by a student) / (Total number of subjects)

"""

N, X = map(int, input().split(" "))

scores = []

for _ in range(X): # saving the inputs in a list of lists
    a = list(map(float, input().split(" ")))
    scores += [a]

for score in zip(*scores): # finds the average of each sublist
    print(sum(score)/float(X))
    
