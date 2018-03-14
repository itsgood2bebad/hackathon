import pandas as pd
import matplotlib.pyplot as plt

date = pd.read_csv("df_date.csv")
#print(date)
print(date.dtypes)
print (date.columns)
date.columns = [x.lower() for x in date.columns]
date.columns =[x.replace(' ','') for x in date.columns]
print(date.columns)
print(date.time[1][5:9])
date.time = pd.to_datetime(date.time)
date.time.dt.month[0]
date.time.dt.day[0]
date.time.dt.hour[0]
date.time.dt.minute[0]
for j in date.time:
    i =0
   while i < len(i):
    if i
print(i)
#date.time.sort_values(ascending=False)
date.time.sort_values(ascending=True)
date.time.hist()