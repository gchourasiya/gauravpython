# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[1])):
        result[j][i]=X[i][j]
print(result)


''' Program to transpose a matrix using list comprehension'''

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

print(result)