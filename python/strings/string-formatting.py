# Author: kmmcelro
# This is my solution to the Hackerrank challenge, String Formatting
# link: https://www.hackerrank.com/challenges/python-string-formatting/problem

""""
Task

Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
"""

def print_formatted(number):
    b = str(bin(number))
    colwidth = len(b[2:]) + 1
    space = " "
    for i in range(1,number+1):
        # converting to the formats and making them strings
        decimal = str(i)
        octal = str(oct(i))
        hexad = str(hex(i))
        binary = str(bin(i))
        # cuts off the indentifier characters to match format
        octal = octal[2:]
        hexad = hexad[2:]
        hexad = hexad.upper() # makes the letters capital
        binary = binary[2:]
        # adding appropriate number of spaces in front of each number and combining into line string
        nd = (colwidth - len(decimal)-1) * space
        no = (colwidth - len(octal)) * space 
        nh = (colwidth - len(hexad)) * space
        nb = (colwidth - len(binary)) * space
        line = nd + decimal + no + octal + nh + hexad + nb + binary 
        print(line) # prints the line
    return 

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)