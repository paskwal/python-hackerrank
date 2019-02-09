# -*- coding: utf-8 -*-
# 
# https://www.hackerrank.com/challenges/python-lists/problem

# Problem
# Consider a list (list = []). You can perform the following commands:
#   insert i e: Insert integer  at position .
#   print: Print the list.
#   remove e: Delete the first occurrence of integer .
#   append e: Insert integer  at the end of the list.
#   sort: Sort the list.
#   pop: Pop the last element from the list.
#   reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
# The first line contains an integer, n, denoting the number of commands. 
# Each line i of the n subsequent lines contains one of the commands described above.

LIST = []

def do_operation(operation):
    if len(operation)==0:
        return
    if   operation[0] == "print":
        print(LIST)
    elif operation[0] == "insert":
        if len(operation) != 3:
            return
        else:
            LIST.insert(int(operation[1]), int(operation[2]))
    elif operation[0] == "remove":
        if len(operation) != 2:
            return
        else:
            LIST.remove(int(operation[1]))
    elif operation[0] == "append":
        if len(operation) != 2:
            return
        else:
            LIST.append(int(operation[1]))
    elif operation[0] == "sort":
        LIST.sort()
    elif operation[0] == "pop":
        LIST.pop()
    elif operation[0] == "reverse":
        LIST.reverse()





if __name__ == '__main__':
    N = int(input())

    for line_in in range(N):
        next_operation = input().split()
        # (operation, b) = next_operation.split()
        do_operation(next_operation)
    







