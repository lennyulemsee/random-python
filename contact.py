#!/usr/bin/python3

'''
Problem Statement:

When we share our phone numbers with others, we share the numbers digit by digit.

Given a phone number in words, convert the number to digits.
For example, convert “six four eight three” to “6483”.

All phone numbers will be 10 digits.
Two repeating digits will be shortened using the word “double”. Three repeating
digits will be shortened using the word “triple”. If the digits repeat four or more
times, they will be shortered using ‘double’ and ‘triple’ mutiple times.
'''
# PSEUDOCODE
# create an array of words zero to nine
# whenever a word is named, return it's index
# add the index to a string as a character
# if there is a given word is double, do it twice. if tripple, thrice.
# convert the string of the resulting numbers into integer and return it.

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getNums(names):
    i = 0
    contactStr = ''
    
    while i < len(names):
        if names[i] in words:
            contactStr += str(words.index(names[i]))
        elif names[i] == "double":
            i += 1
            contactStr += str(words.index(names[i])) * 2
        elif names[i] == "tripple":
            i += 1
            contactStr += str(words.index(names[i])) * 3
        i += 1
    return int(contactStr)


test1 = ["nine", "one", "two", "three", "four", "five", "six", "seven", "eight", "zero"]
test2 = ["nine", "double", "two", "three", "four", "five", "six", "seven", "eight", "zero"]
test3 = ["nine", "tripple", "three", "four", "five", "six", "seven", "eight", "zero"]
print(getNums(test1))
print(getNums(test2))
print(getNums(test3))
