import csv
import pandas as pd
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
csvwritefile = 'cswout.csv'

'''
#Approach 1
with open(csvwritefile,'w',newline='') as csvdata:      #File object
    csvwriter = csv.writer(csvdata)                     #csv write object
    csvwriter.writerow(header)
    csvwriter.writerows(data)
'''

'''
#Approach 2
with open(csvwritefile,'w') as csvdata:      #File object
    for header in header:
        csvdata.write(str(header)+', ')
    csvdata.write('\n')
    for data in data:
        for row in data:
            csvdata.write(str(row) + ', ')
        csvdata.write('\n')

'''

#Approach 3
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
df = pd.DataFrame(data,columns=header)
df.to_csv('student.csv',encoding='utf-8')
