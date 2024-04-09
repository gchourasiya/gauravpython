import pandas as pd
import  sqlite3
import json

sqlite_file = file
connection = sqlite3.connect(sqlite_file)

logDB_absnull = pd.read_sql_query("select * from LOG where event in (1,2,3) and time is not null ORDER by time desc",connection)
logDB_absnull.fillna(value=pd.np.nan,inplace=True)
logDB_absnull = logDB_absnull.replace(pd.np.nan, "None",regex=False)
logDB_absnull = logDB_absnull.replace(r'nan', "None",regex=True)
logDB_absnull = logDB_absnull.replace(r'NaN', "None",regex=True)
logDB_absnull = logDB_absnull.replace(r'^\s*$', "None",regex=True)
logDB_absnull = logDB_absnull.replace(pd.np.nan, "None",regex=False)
logDB_absnull = logDB_absnull.replace(pd.np.nan, "None",regex=False)
