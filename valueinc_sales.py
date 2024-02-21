# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:34:29 2024

@author: nyangang
"""

import pandas as pd
data = pd.read_csv(r'transactions.csv')
data.info()
data = pd.read_csv(r'transactions.csv',sep=';')
 
# Summary of the dataset
data.info()
 
var1 = ['apple','pear','oranges'] # list
var= (1,2,3,4)# Tupple
print(var)
print(var1)

# Dictionary
var2 = {'Name':'Godlove', 'Location':'South Africa', 'Age':52}
print(var2)

# Set
var3 = {'john','paul','peter','james'}
print (var3)
# Boolean
var4 = True

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6
# Mathmatical calculations on Tableau
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

#Adding a new column to a dataframe
data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
 
# Markup = sales-cost / cost

data['markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']
data['markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']

# Rounding Markup

roundmarkup = round(data['markup'], 2)
data['markup'] = round(data['markup'], 2)

#Combining data fields(day-month-year)with concatination

my_date = 'Day' + '-'  +'Month' + '-' +'Year'# Day and Year are int and be changed to string
print(data['Year'].dtype)

# Change Data Type to string
day = data['Day'].astype(str)
year = data['Year'].astype(str) 
print(day.dtype)# check data type

my_date = day+'-'+data['Month']+'-'+year # dy, month, year combined
data['Date'] = my_date

# Using iloc to view specific columns and rows
data.iloc[0] # Views the first row with index 0
data.iloc[0:3] # Views rows 0,1,2
data.iloc[-5:] # Views the last five rows
data.head(5)# Views first five rows
data.iloc[:,2]# Views all rows in column 2
data.iloc[4,2]# views 4th row of second column

# Split the Clientkeywords with the SPLIT FUNCTION
split_col = data['ClientKeywords'].str.split(',' , expand=True)

# Creating new titles for the split columns
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['Length of Contract'] = split_col[2]

# Remove square bracket from ClientAge with Replace Function. 
# Note that same method can be used to replace other keyword in title for eg
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['Length of Contract'] = data['Length of Contract'].str.replace(']', '')

# Using lower function to change items to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()
data['ItemDescription'][0:2]

# Joining a new dataset to the main datafile
# Import the new data set
import pandas as pd
seasons=pd.read_csv('value_inc_seasons.csv',sep=';')
data=pd.merge(data,seasons,on='Month')

#Dropping Columns
data = data.drop('Day', axis=1)
data = data.drop('ClientKeywords', axis=1)
data = data.drop('Month', axis=1)
data =data.drop('Year', axis=1)

df = pd.DataFrame(data)

# Dropping the 'ClientKeywords' column
df.drop(columns=['Month'], inplace=True)

print(df)

# Exporting the data file into csv
data.to_csv('valueinc_cleaned.csv', index=False)# inex is false because we do not need index column

































