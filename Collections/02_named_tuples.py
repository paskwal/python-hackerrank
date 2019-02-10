# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# Problem
# Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
# Your task is to help Dr. Wesley calculate the average marks of the students.
# Average = Sum of all marks / Total Students

# Note: 
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet. 
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

# Input Format
# The first line contains an integer N, the total number of students. 
# The second line contains the names of the columns in any order. 
# The next N lines contains the marks, IDs, name and class, under their respective column names.

# Output Format
# Print the average marks of the list corrected to 2 decimal places.

from collections import namedtuple

column_names = ['ID', 'MARKS', 'CLASS', 'NAME']
Student = namedtuple('Student','ID MARKS CLASS NAME')
Students = []

if __name__ == '__main__':
    N = int(input())
    Columns = input().split()
    average = 0

    for _ in range(N):
        data = input().split()
        student_dict = {}
        for i in range(len(column_names)):
            student_dict[Columns[i]] = data[i] 

        student = Student(  ID    = student_dict['ID'], 
                            MARKS = student_dict['MARKS'],
                            CLASS = student_dict['CLASS'],
                            NAME  = student_dict['NAME'])
        
        Students.append(student)
        average += float(getattr(student,'MARKS'))
    print("%.2f" % (float(average) / len(Students)))
