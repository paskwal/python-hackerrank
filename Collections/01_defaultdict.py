# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Problem
# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. 
# There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
# Print the indices of each occurrence of m in group A. If it does not appear, print -1.


# Input Format
# The first line contains integers, n and m separated by a space. 
# The next n lines contains the words belonging to group A. 
# The next m lines contains the words belonging to group B.

# Output Format
# Output m lines. 
# The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.

from collections import defaultdict

if __name__ == '__main__':
    A = []
    B = []
    d = defaultdict(list)

    n, m = map(int, input().split())
    for _ in range(n):
        A.append(input())
    for _ in range(m):
        B.append(input())

    for e in B:
        if e in d.keys():
            continue
        A2 = A.copy()
        count = A2.count(e)
        if count == 0:
            d[e].append(-2)
        else:
            d[e].append(A2.index(e))
            index = A2.index(e)
            shift = 0
            while(count>1):
                count -=1
                A2.remove(e)
                shift += 1
                d[e].append(A2.index(e) + shift)

    for e in B:
        print(' '.join(str(x + 1) for x in d[e]))



