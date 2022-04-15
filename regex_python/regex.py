import re

'''
#Search the string to see if it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
result = re.search(r'^The.*Spain$', txt)
if result :print('True')
else:print('False')
'''

'''
#''Find all lower case characters alphabetically between "a" and "m"
import re
txt = "The rain in Spain"
result = re.findall('[a-m]',txt)
print(result)
'''


'''
#Find all digit characters:
txt = "That will be 59 dollars"
result = re.findall(r'\d',txt)
print(result)
'''


'''
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
txt = "hello planet"
result = re.findall('^he..o', txt)
print(result)
'''

'''
# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")
print(match.group())
'''

'''
# A sample text string where regular expression
# is searched.
string  = """Hello my Number is 123456789 and
             my friend's number is 987654321"""
regex = r'\d+'
match = re.findall(regex, string)
print(match)
'''

'''
# starting index and the ending index of the string portal.
s = 'GeeksforGeeks: A computer science portal for geeks'
pattern = r"portal"

match = re.search(pattern,s)
print(match.start())
print(match.end())
'''


'''
s = 'geeks.forgeeks'
regex = r"."
# match = re.search(regex,s)
match = re.search(r'\.', s)
print(match.group(0))
'''

'''
#Usage of compile in regex
regex = re.compile(r"[a-e]")
print(regex.findall("Aye, said Mr. Gibenson Stark"))
'''

'''
string = "GeeksForGeeks"
pattern = r"[@_!#$%^&*()<>?/\;|}{~:]"
regex = re.compile(pattern)
if not regex.search(string):
    print("Does not contain special characters.")
else:
    print("Contains special characters.")
'''


'''
#email address check
#gautav+_-1234chgs@email.com
regex = 
'''
