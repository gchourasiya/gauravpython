'''
Python Program to Check Two Strings are Anagram or Not
'''
str1= 'listen'
str2='silent'

if sorted(list(str1)) == sorted(list(str2)):
    print("Anagram")
else:
    print("Not Anagram")