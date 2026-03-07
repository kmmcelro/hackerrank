# Author: kmmcelro
# This task is apart of the ProjectEuler+ Contest on Hackerrank
# This is my solution to Project Euler #11: Largest product in a grid
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem

""""
Task
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
"""

#!/bin/python3

import sys

# the four directions to check the product to get full coverage (other directions would mean double counting)
def upper_diag(x, y, grid_x): # up to the right 
    return grid_x[y][x] * grid_x[y-1][x+1] * grid_x[y-2][x+2] * grid_x[y-3][x+3]
    
def lower_diag(x, y, grid_x): # down to the right
    return grid_x[y][x] * grid_x[y+1][x+1] * grid_x[y+2][x+2] * grid_x[y+3][x+3]
    
def right(x, y, grid_x):
    return grid_x[y][x] * grid_x[y][x+1] * grid_x[y][x+2] * grid_x[y][x+3]
    
def down(x, y, grid_x):
    return grid_x[y][x] * grid_x[y+1][x] * grid_x[y+2][x] * grid_x[y+3][x]

def maxProd(grid_x, n):
    max_prod = 0
    # checking each spot by the directions they have available to check and checking the spot's max prod against current max_prod
    for i in range(0, n-3):
        for j in range(0, n):
            if j < 3:
                prod = max([lower_diag(i, j, grid_x), right(i, j, grid_x), down(i, j, grid_x)])
            elif j < n-3:
                prod = max([upper_diag(i, j, grid_x), lower_diag(i, j, grid_x), right(i, j, grid_x), down(i, j, grid_x)])
            else:
                prod = max(upper_diag(i, j, grid_x), right(i, j, grid_x)) 
            if prod > max_prod:
                max_prod = prod
    for i in range(n-3, n):
        for j in range(0, n-3):
            if down(i, j, grid_x) > max_prod:
                max_prod = down(i, j, grid_x)
    return max_prod
            
            

grid = []
n = 20 # change for different grid size
for grid_i in range(n):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

print(maxProd(grid, n))