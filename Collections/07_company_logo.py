# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

# https://www.hackerrank.com/challenges/most-commons/problem

# Problem
# A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
# They are now trying out various combinations of company names and logos based on this condition. Given a string , which is 
# the company name in lowercase letters, your task is to find the top three most common characters in the string.
#       - Print the three most common characters along with their occurrence count.
#       - Sort in descending order of occurrence count.
#       - If the occurrence count is the same, sort the characters in alphabetical order.
# For example, according to the conditions described above, GOOGLE would have it's logo with the letters G, O, E.

# Input Format
# A single line of input containing the string S.

# Output Format
# Print the three most common characters along with their occurrence count each on a separate line. 
# Sort output in descending order of occurrence count. 
# If the occurrence count is the same, sort the characters in alphabetical order.


from collections import OrderedDict

if __name__ == '__main__':
    d = {}
    sorted_by_value = OrderedDict(sorted(d.items(), key=lambda t: t[1]))

    letters_occurence = OrderedDict()
    string_S = input()

    occurences = {}
    letters = []

    for letter in string_S:
        if letter in letters:
            occurences[letter] += 1
        else:
            occurences[letter] = 1
            letters.append(letter)

        if letter in letters_occurence.keys():
            letters_occurence[letter] -= 1
        else:
            letters_occurence[letter] = -1
    


    # Sort in descending order of occurrence count
    sorted_by_value = OrderedDict(sorted(letters_occurence.items(), key=lambda t: (t[1], t[0]), reverse=False))
    for i in range(3):
        key, value = sorted_by_value.popitem(last=False)
        print(key,value * -1)

#    print()


    sorted_by_value = OrderedDict(sorted(sorted(letters_occurence.items(), key=lambda t: t[1], reverse=True), key=lambda t:t[0], reverse=False))
    # TODO If the occurrence count is the same, sort the characters in alphabetical order. 

    for i in range(3):
        key, value = sorted_by_value.popitem(last=False)
#        print(key,value)

#    print()
    sorted_by_value = OrderedDict(sorted(letters_occurence.items(), key=lambda t: t[0], reverse=False))

    for i in range(3):
        key, value = sorted_by_value.popitem(last=False)
#        print(key,value)

    for i in range(3):
        letter = letters.pop()
#        print(letter, occurences[letter])



