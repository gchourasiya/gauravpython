import pandas as pd
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class TestDataValidation:

    @keyword('get selenium robot driver')
    def getDriver(self):
        seleniumlib = BuiltIn().get_library_instance('Selenium2Library')
        return seleniumlib


    @keyword('read csv file and return dataframe')
    def readCsv(self,csvfile):
        df = pd.read_csv(csvfile)
        return df

    @keyword("GET-DATAFRAME")
    def getDataFrame(self,header,rows):
        df = pd.DataFrame(data=rows,columns=header)
        return df
    @keyword("Format number of cases values")
    def formatNumberOfCasesColumnValues(self,x):
        if str(x).endswith('k') or str(x).endswith('K'):
            x_half = x[:-1]
            x = float(x_half)*1000
            x = int(x)
            return str(x)
        elif str(x).endswith('M') or str(x).endswith('m'):
            x_half = x[:-1]
            x = float(x_half)*1000000
            x = int(x)
            return str(x)
        elif str(x).endswith('B') or str(x).endswith('b'):
            x_half = x[:-1]
            x = float(x_half)*1000000000
            x = int(x)
            return str(x)
        else:
            return x

    def regularizeNoOfCasesValues(self,df):
        # df = self.readCsv(csv)
        df['number of cases'] = df['number of cases'].apply(lambda x: self.formatNumberOfCasesColumnValues(x))
        df['number of cases'] = df['number of cases'].astype(str).astype(int)
        df.sort_values(by='number of cases', inplace=True)
        df = df.reset_index(drop=True)
        return df

    def sortByColName(self,df,colName):
        colName = colName.lower()
        if colName in df.columns:
            df.sort_values(by=colName, inplace=True)
            df = df.reset_index(drop=True)
            return df
        else:
            return False
    def filterData(self,df,colName,searchstr):
        searchstr = str(searchstr).lower()
        colName = colName.lower()
        df[colName] = self.convertDfValuestoLower(df[colName])
        df = df[df[colName].str.contains(searchstr)]
        return df



    def convertTodf(self,headerlen,lst):
        lstX = [lst[0].split('\n')]
        lst3 = lstX[0]

        lst2 = [lst3[i:i + headerlen] for i in range(0, len(lst3), headerlen)]

        df = pd.DataFrame(lst2[1:], columns=lst2[0])
        df.columns = [x.lower() for x in df.columns]

        return df
    def getDataType(self,df,colName):
        colName = colName.lower()
        dataType = df[colName].dtype
        return dataType

    @keyword('convert2string')
    def convert2String(self,df,colName):
        colName = colName.lower()
        df[colName] = df[colName].astype(str)
        df = self.sortByColName(df,colName)
        return df

    def convertDfValuestoLower(self,df):
        # df = df.applymap(lambda s: s.lower() if type(s) == str else s)
        df = df.str.lower()
        return df
