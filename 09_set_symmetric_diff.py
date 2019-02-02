# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Task
# Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper. 
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper. 
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

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

    print(len(setA.symmetric_difference(setB)))
~
~
