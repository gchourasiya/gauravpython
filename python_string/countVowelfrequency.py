str1 = "Write a program to accept a string and count the frequency of each vowel"
str1 = str1.lower()
# Lst = str1.split()
print(str1)
vowelFreq = {'a':0,'e':0,'i':0,'o':0,'u':0}
for char in str1:
    if char in vowelFreq.keys():
        vowelFreq[char]+=1
print(vowelFreq)
