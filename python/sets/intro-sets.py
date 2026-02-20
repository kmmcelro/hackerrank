# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Introduction to Sets
# link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

""""
Task
Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Formula used:
Average = Sum of Distinct Heights / Total Number of Distinct Heights

"""


def average(array):
    uniqArray = set(array)
    total = 0
    count = 0
    for i in uniqArray:
        total += float(i)
        count += 1.0
    result = total / count
    result = round(result, 3)
    return result
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)