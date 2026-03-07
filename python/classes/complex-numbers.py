# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Classes: Dealing with Complex Numbers
# link: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

""""
Task
For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

Use class structure for this.
"""
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        Cresult = Complex(0, 0)
        Cresult.real =  self.real + no.real
        Cresult.imaginary = self.imaginary + no.imaginary
        return Cresult
    
    def __sub__(self, no):
        Cresult = Complex(0, 0)
        Cresult.real =  self.real - no.real
        Cresult.imaginary = self.imaginary - no.imaginary
        return Cresult
    
    def __mul__(self, no):
        Cresult = Complex(0, 0)
        Cresult.real =  self.real * no.real - self.imaginary * no.imaginary
        Cresult.imaginary = self.imaginary * no.real + no.imaginary * self.real
        return Cresult
    
    def __truediv__(self, no):
        Cresult = Complex(0, 0)
        Cresult.real =  (self.real * no.real + self.imaginary * no.imaginary) / (no.real * no.real + no.imaginary * no.imaginary)
        Cresult.imaginary = (self.imaginary * no.real - self.real * no.imaginary) / (no.real * no.real + no.imaginary * no.imaginary)
        return Cresult
    
    def mod(self):
        Cresult = Complex(0, 0)
        Cresult.real = math.sqrt(self.real * self.real + self.imaginary * self.imaginary)
        return Cresult
    
    def __str__(self): # converting complex values to a string
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')