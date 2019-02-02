#!/bin/python3

N = int(input())

if (N>100 or N <1):
    exit(0)
if (N % 2 != 0): # N is odd
    print("Weird")
else:
    if (N<=5 and N>=2):
        print("Not Weird")
    elif (N>=6 and N<=20):
        print("Weird")
    else:
        print("Not Weird")
      

