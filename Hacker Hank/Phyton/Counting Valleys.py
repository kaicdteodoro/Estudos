#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step.
# Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude.

def countingValleys(steps, path):
 mar = 0
 qntD = 0
 ctr = False
 cord = list(path)
 for i in range(steps):]
     if cord[i] == "U":
         mar = mar + 1
     elif cord[i] == "D":
         mar = mar - 1
     if mar < 0 and ctr == False:
         qntD = qntD + 1
         ctr = True
     if ctr == True and mar > -1:
         ctr = False
 return qntD
# Write your code here
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
