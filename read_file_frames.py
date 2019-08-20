import csv
import pandas as pd 
import numpy
import glob
from array import array
from pathlib import Path

C_data = pd.read_csv("cc.csv") 
D_data = pd.read_csv("dd.csv")
frames = [C_data, D_data]
df = pd.concat(frames)
#from collections import Counter

#---------------------------------------------------------------------
#Reach csv and create a data frame with dates
#---------------------------------------
df.set_index('Invoice Date', inplace=True)
df.index = pd.to_datetime(df.index)
types_dict = {'USD Extended': float, 'CostUS01Domain': float}
for col, col_type in types_dict.items():
         df[col] = df[col].astype(col_type)
         print(col_type)
    
profitloss=df['USD Extended'] -df['CostUS01Domain'] 
df.insert(5, "ProfitLoss", profitloss, True)
#df_clp=df["Time","USD Extended","CostUS01Domain","ProfitLoss"]


plt1=df[['USD Extended','CostUS01Domain','ProfitLoss']].plot(title="Daily Sales Profit/Loss")
#plt1.set_ylabel="Expenditure in Dollars"
#plt1.set_xlabel="Time"

plt1.set(xlabel="Time", ylabel="Dollars")

mm=df.resample('1M').mean()
x=mm.index
y=mm['ProfitLoss']

plt2=mm[['USD Extended','CostUS01Domain','ProfitLoss']].plot(title="Monthly Sales Profit/Loss")
plt2.set(xlabel="Time", ylabel="Dollars")

#ax = mm.plot(lw=2, color=['grey','grey','red'], marker='.',markersize=10, title='Costs and Profit')
#ax.set_ylabel("Expenditure in Dollars ")
#mm.index.name = 'Time'
print(f'Processed {line_count} lines.', line_count)
    #profit=numpy.subtract(uextended, costdomain)
    #print(profit)
    
    
    
 #   profit=  uextended - costdomain
    