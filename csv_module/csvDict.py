import csv
import pandas as pd
csvfile = 'username.csv'

df = pd.read_csv(csvfile)
df.to_html('temp.html')