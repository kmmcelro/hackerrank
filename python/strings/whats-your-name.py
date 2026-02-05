# Author: kmmcelro
# This is my solution to the Hackerrank challenge, What's Your Name?
# link: https://www.hackerrank.com/challenges/whats-your-name/problem

""""
Task
Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
"""


#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    name = first + " " + last 
    print ("Hello " + name + "! You just delved into python.")
    return

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)