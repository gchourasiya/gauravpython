#Write a program to display the smallest word from the string.

str1 = "Write a program to display the smallest word from the string."
str1 = str1.casefold()
print(str1)

def getLen(str):
    return len(str)

out = sorted(str1.split(),key=getLen)
print(out[0])