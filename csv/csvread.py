import csv
from turtle import bye

import pandas as pd
csvfile = 'email.csv'
'''
#Approach 1
with open(csvfile) as csvfile:          #original File handling object
    csvdata = csv.reader(csvfile)       #csv handling object
    header = []
    header=next(csvdata)
    print("Header :",header)
    rows =[]
    for row in csvdata:
        rows.append(row)
    print("Rows :",rows)
'''


'''
#Approach 2

with open(csvfile) as csvfile:
    csvdata = csvfile.readlines()
    header = csvdata[0]
    print(header)

    rows = csvdata[1:]
    print(rows)

'''

#Approach 3
df = pd.read_csv(csvfile)
print(df)
