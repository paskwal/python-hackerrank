# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

# Input Format
# The first line contains n, the number of students who have subscribed to the English newspaper. 
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper. 
# The fourth line contains b space separated roll numbers of those students.

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    setA = set()
    setB = set()

    n = int(input())
    elements = input()
    elements_list = elements.split()
    setA.update(elements_list)


    b = int(input())
    elements = input()
    elements_list = elements.split()
    setB.update(elements_list)

    print(len(setA.intersection(setB)))
