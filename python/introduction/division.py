# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Python: Division
# link: https://www.hackerrank.com/challenges/python-division/problem

""""
Task
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b) 
    print(a/b)
