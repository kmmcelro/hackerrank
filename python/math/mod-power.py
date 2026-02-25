# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Power - Mod Power
# link: https://www.hackerrank.com/challenges/python-power-mod-power/problem

""""
Task
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

"""

a = int(input())
b = int(input())
m = int(input())

print(a**b)
print(pow(a,b,m))