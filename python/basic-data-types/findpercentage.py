# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Finding the Percentage
# link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

""""
Task
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = 0.0
    for i in range(0,3): # each student has 3 scores
        average += student_marks[query_name][i]
    average = average / 3.0
    print("%.2f" % average)