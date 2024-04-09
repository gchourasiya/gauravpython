import pandas as pd

dict1 = {"a" : [5, 4, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]}

index =  [1, 2, 3]

df = pd.DataFrame(dict1,index=index)
print(df)

print('\n')
print("SORTED DF")
df.sort_values(by='a',inplace=True,ascending=False)



df.sort_index(inplace=True)
print(df)

print('\n')
print("RESET INDEX")

df.reset_index(inplace=True)
print(df
      )

