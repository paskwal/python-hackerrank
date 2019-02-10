# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

# https://www.hackerrank.com/challenges/piling-up/problem

# Problem
# There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. 
# The new pile should follow these directions: if cube_i is on top of cube_j then sideLength_j > sideLength_i.
# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

# Input Format
# The first line contains a single integer T, the number of test cases. 
# For each test case, there are 2 lines. 
# The first line of each test case contains n, the number of cubes. 
# The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

# Output Format
# For each test case, output a single line containing either "Yes" or "No" without the quotes.

from collections import deque

# import sys
# sys.setrecursionlimit(100001)

def checkPilingUpLocal(d):
    last = max(d)
    while True:
        if len(d) < 2:
            return True
        left,right = d[0], d[-1]

        if left > last or right > last:
            return False
        elif left < right:
            d.pop()
            last = right
        elif right < left:
            d.popleft()
            last = left
        else:
            d.pop()
            d.popleft()
            last = left                        

def checkPilingUpRecursive(d):
    if len(d) < 2:
        return True
    left,right,m = d[0], d[-1], max(d)
    if left < m and right < m:
        return False
    elif left < right:
        d.pop()
        return checkPilingUpRecursive(d)
    elif right < left:
        d.popleft()
        return checkPilingUpRecursive(d)
    else:
        d.pop()
        d.popleft()
        return checkPilingUpRecursive(d)

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        numbers = map(int, input().split())

        d = deque()
        d.extend(numbers)

        if checkPilingUpLocal(d):
            print("Yes") 
        else:
            print("No")



