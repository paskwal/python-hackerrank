# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

# https://www.hackerrank.com/challenges/np-array-mathematics/problem

# Task
# You are given two integer arrays, A and B of dimensions NxM. 
# Your task is to perform the following operations:
# Add (A + B)
# Subtract (A - B)
# Multiply (A * B)
# Integer Division (A / B)
# Mod (A % B)
# Power (A ** B)

# Input Format
# The first line contains two space separated integers, N and M. 
# The next N lines contains M space separated integers of array A. 
# The following N lines contains M space separated integers of array B.

# Output Format
# Print the result of each operation in the given order under Task.


import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    tmp = []
    for _ in range(n):
        line = list(map(int, input().split()))
        tmp.append(line)
    a = numpy.array(tmp)

    tmp = []
    for _ in range(n):
        line = list(map(int, input().split()))
        tmp.append(line)
    b = numpy.array(tmp)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)


