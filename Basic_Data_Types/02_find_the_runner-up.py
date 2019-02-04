# -*- coding: utf-8 -*-
# 
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Task
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# < 02_test_case_00.txt
# 5

if __name__ == '__main__':
    n = int(input())
#    arr = map(int, input().split())
    elements = input()
    elements_list = [int(e) for e in elements.split()]

    m = max(elements_list)
    count = elements_list.count(m)
    for i in range(count):
        elements_list.remove(m)
    
    print(max(elements_list))



