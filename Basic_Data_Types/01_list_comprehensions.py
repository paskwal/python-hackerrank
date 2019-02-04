# -*- coding: utf-8 -*-
# 
# https://www.hackerrank.com/challenges/list-comprehensions/problem

# Task
# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of
# a cuboid along with an integer N. You have to print a list of all possible coordinates given by (i,j,k) on
# a 3D grid where the sum of X + Y + Z is not equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z.

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# < 01_test_case_00.txt
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# < 01_test_case_01.txt
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ( (i+j+k != n))]

    print(result)


# [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
