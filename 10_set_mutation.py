# -*- coding: utf-8 -*-
# 
# # https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Task
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
# Your task is to execute those operations and print the sum of elements from set A.

# Input Format
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
#   The first line of each part contains the space separated entries of the operation name and the length of the other set.
#   The second line of each part contains space separated list of elements in the other set.

# < 10_test_case_1.txt
# 38 

def do_operation2(operation, setA, setB):
    switcher = {
        "update": do_update(setA, setB),
        "intersection_update": do_intersection_update(setA, setB),
        "symmetric_difference_update": do_symmetric_difference_update(setA, setB),
        "difference_update": do_difference_update(setA, setB),
    }
    return switcher.get(operation, None)

def do_operation(operation, setA, setB):
    if operation == "update":
        do_update(setA, setB)
    elif operation == "intersection_update":
        do_intersection_update(setA, setB)
    elif operation == "symmetric_difference_update": 
        do_symmetric_difference_update(setA, setB)
    elif operation == "difference_update": 
        do_difference_update(setA, setB)

def do_update(setA, setB):
    setA.update(setB)

def do_intersection_update(setA, setB):
    setA.intersection_update(setB)

def do_difference_update(setA, setB):
    setA.difference_update(setB)

def do_symmetric_difference_update(setA, setB):
    setA.symmetric_difference_update(setB)

def calc_sum(setA):
    result = 0
    for e in setA:
        result += int(e)
    return result


if __name__ == '__main__':
    setA = set()

    setA_size = int(input())
    elements = input()
    elements_list = elements.split()
    setA.update(elements_list)

    nb_operations = int(input())
    for i in range(nb_operations):
        setB = set()
        next_operation = input()
        (operation, b) = next_operation.split()
        elements = input()
        elements_list = elements.split()
        setB.update(elements_list)

        do_operation(operation, setA, setB)

    print(calc_sum(setA))
