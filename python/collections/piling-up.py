# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Piling Up!
# link: https://www.hackerrank.com/challenges/piling-up/problem

""""
Task
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. 
The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[k] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

"""

# Setting up the inputs
T = int(input())

for i in range(0,T):
    n = int(input())
    sideLength = [int(x) for x in input().split(" ")]
    result = "Yes" # Defaults to Yes if the stacking is possible (loop finishes without break)
    # Picking the first block for the stack
    if sideLength[0] >= sideLength[n-1]:
        comp = sideLength.pop(0)
    else:
        comp = sideLength.pop(n-1)
    # Simulating the stacking
    for nstep in range(n-2,0,-1):
        if comp >= sideLength[0] and comp >= sideLength[nstep]:
            if sideLength[0] >= sideLength[nstep]:
                comp = sideLength.pop(0)
            else:
                comp = sideLength.pop(nstep)
        # If there is a higher number in the edges than is on the top of the stack the result is no
        else: 
            result = "No"
            break
    print(result)
