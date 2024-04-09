#Write a program to display the unique words from the string.

str1= "Write a program to display the unique words from the string the string display progRam write"

lst = str1.split()
newLst = []

for i in lst:
    i = i.lower()
    if i not in newLst:
        newLst.append(i)
for i in newLst:
    print(i,end=" ")