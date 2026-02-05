# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Find a String
# link: https://www.hackerrank.com/challenges/find-a-string/problem

""""
Task
In this challenge, the user enters a string and a substring. 
ou have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""

def count_substring(string, sub_string):
    k = 0 # tracks number of cases substring appears
    for i in range(0, len(string)):
        if string.startswith(sub_string,i,i+len(sub_string)): #checks if the substring matches with indice i
            k += 1
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)