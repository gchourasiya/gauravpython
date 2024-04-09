#Write a program to accept a string and replace all spaces by ‘#’ symbol

str1 =  "Write a program to accept a string and replace all spaces by ‘#’ symbol"

str2 = ''
for i in str1:
    if i.isspace():
        str2+='#'
    else:
        str2+=i

print(str2)