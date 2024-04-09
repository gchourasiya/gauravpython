#Write a program to display the largest word from the string.

str1 = "Write a program to display the largest word from the string"

Lst = str1.split()
def getLen(str):
    return len(str)
print(sorted(Lst,key=getLen,reverse=True)[0])