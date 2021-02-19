#!/bin/python3

import os
import sys

#A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget.
# Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
 prices = []
 for i in range(len(keyboards)):
     for j in range(len(drives)):
         x = keyboards[i] + drives[j]
         if x <= b:
             prices.append(x)
 if not prices:
     result = -1
 else:
    result = max(prices)
 return result
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
