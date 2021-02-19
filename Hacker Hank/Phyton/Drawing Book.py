#!/bin/python3

import os
import sys

#A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book.
#  They always turn pages one at a time. When they open the book, page  is always on the right side.When they flip page , they see pages  and . 
# Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book.
#  If the book is  pages long, and a student wants to turn to page , what is the minimum number of pages to turn? They can start at the beginning or the end of the book. 
# Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .

# Complete the pageCount function below.
#
def pageCount(n, p):
 contR = 0
 contL = 0
 for i in range(1,n,2):
     if i == p or (i-1) == p:
         break
     contR+=1
 if n%2 == 0:
     x = 1
 else:
     x = -1
 for i in range(n,1,-2):
     if i == p or (i+x) == p:
         break
     contL+=1
 if contR < contL:
     return contR
 else:
    return contL
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
