# -*- coding: utf-8 -*-
# 


# Problem
# You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
# The marks can be floating values. The user enters some integer N followed by the names and marks for N students. 
# You are required to save the record in a dictionary data type. The user then enters a student's name. 
# Output the average percentage marks obtained by that student, correct to two decimal places.

# Input Format
# The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student
# separated by a space. The final line contains the name of a particular student previously listed.

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks.keys():
        print("%.2f" % mean(student_marks[query_name]))

