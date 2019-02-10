# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

# https://www.hackerrank.com/challenges/py-collections-deque/problem

# Task
# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format
# The first line contains an integer N, the number of operations. 
# The next N lines contains the space separated names of methods and their values.

# Output Format
# Print the space separated elements of deque d.


from collections import deque

d = deque()

def do_operation(operation):
    if len(operation)==0:
        return None
    if   operation[0] == "pop":
        return d.pop()
    elif   operation[0] == "popleft":
        return d.popleft()   
    elif operation[0] == "append":
        if len(operation) != 2:
            return None
        else:
            d.append(operation[1])
            return True
    elif operation[0] == "appendleft":
        if len(operation) != 2:
            return None
        else:
            d.appendleft(operation[1])
            return True
    elif operation[0] == "reverse":
        d.reverse()
        return True
    elif operation[0] == "clear":
        d.clear()
        return True
    else:
        return None

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        next_operation = input().split()
        do_operation(next_operation)
        
    print(" ".join(d))

