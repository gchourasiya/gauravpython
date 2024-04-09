str1 ="Write a program to accept two strings from the user and display the common words.(Ignore case)"

str2 =  "Write a program to accept a string and replace all spaces by ‘#’ symbol"
str1 = str1.lower()
str2 = str2.lower()


Lst1 = str1.split()
Lst2 = str2.split()
for i in Lst1:
    if i in Lst2:
        print(i,end=" ")

