import pandas as pd

dict1 = {"a" : [5, 4, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]}

index =  [1, 2, 3]

df = pd.DataFrame(dict1.values(),index=index,columns=dict1.keys())
print(df)

print('\n')
print('DROP COLUMNS')

df.drop(columns='a',inplace=True)
print(df)