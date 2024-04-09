def fun(x):
	dd,mm,yy=x.split('-')
	return int(dd)+int(mm)*100+int(yy)*10000

dates=['15-10-2010',
       '10-1-2000',
       '1-1-2000',
       '25-10-2010']
print(dates)
dates.sort(key=fun)
print(dates)
