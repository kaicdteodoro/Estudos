#!/bin/python3

import math
import os
import random
import re
import sys
# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock,
#  determine how many pairs of socks with matching colors there are.
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
 par = 0
 vet = sorted(set(ar))
 for x in range(len(vet)):
     num = ar.count(vet[x])
     if num % 2 == 0:
         par = par + num/2
     elif num > 0.5:
         par = par + ((num/2) - 0.5)
 
 return int(par)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
