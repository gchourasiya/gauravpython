from itertools import islice
import pandas as pd
lst1 =['NAME\nNUMBER OF CASES\nAVERAGE IMPACT SCORE\nCOMPLEXITY\nMan in the Middle\n95k\n8.12\nhigh\nPassword attack\n32.85M\n5\nlow\nPhishing\n25.12M\n7.18\nlow\nSession hijack\n9024\n5.79\nhigh\nSQL Injection\n1.25M\n10.21\nmedium\nXSS\n29850\n2.19\nlow']
lst = [lst1[0].split('\n')]
lst3= lst[0]
# total_ele = len(lst[0])
# rem = int(total_ele//4)
# print(rem)

lst2 = [lst3[i:i+4] for i in range(0, len(lst3), 4)]
# print(lst2)

df = pd.DataFrame(lst2[1:],columns=lst2[0])
print(df)
