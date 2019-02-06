# -*- coding: utf-8 -*-
# 
# https://www.hackerrank.com/challenges/nested-list/problem

# Problem
# Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) 
# of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.


# Input Format
# The first line contains an integer, N, the number of students. 
# The 2*N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# < 03_test_case_00.txt
# Berry
# Harry


if __name__ == '__main__':
    names_by_grades = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score in names_by_grades.keys():
            names_by_grades[score].append(name)
        else:
            names_by_grades[score] = [name]

    scores = list(names_by_grades.keys())
    scores.remove(min(scores))
    slg = min(scores)

    slg_names = sorted(names_by_grades[slg])
    print('\n'.join(slg_names))

