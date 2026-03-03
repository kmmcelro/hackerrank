# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Collections.namedtuple()
# link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

""""
Task
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.

"""

from collections import namedtuple

numStudents = int(input())

Grades = namedtuple('Grades', list(map(str, input().rsplit()))) # sets the label of columns based on input

scoresTot = 0

for i in range(numStudents):
    gradeBook = Grades(*input().rsplit())  # adds the rows to the gradebook tuple
    scoresTot += int(gradeBook.MARKS) # pulls the mark from the tuple to add to the sum for the average

averScore = scoresTot/numStudents
print("%.2f" % averScore)

