# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:04:00 2024

@author: nyangang
"""
import json
import pandas as pd
json_file = open('loan_data_json.json')
data=json.load(json_file) 
data=pd.DataFrame(data)
loandata=pd.DataFrame(data)

#Finding unique values for the purpose column
loandata['purpose'].unique

#Describe the data
loandata.describe()
loandata['purpose'].describe

#Describe the data for a particular column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#Install numpy from anaconda prompt with pip install numpy
#import numpy
import numpy as np

#Using exponent exp() to get annual income
income=np.exp(loandata['log.annual.inc'])
loandata['annualincome']=income

#Working with array
arr=np.array([1, 2, 3, 4])

#if conditions
#Working with if statements

a=40
b=500
if b>a:
    print('b is greater than a')
    
# Add more conditions
a=40
b=500
c=1000
if b>a and b<c:
    print('b is greater than a but less than c')
    
#What if a condition is not met

a=400
b=500
c=20
if b>a and b<c:
    print('b is greater than a but less than b')
else:
    print('No condition met')
    
a=40
b=0
c=30
if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater a but less than c')
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('No conditions met')
    
# Using OR
a=40
b=500
c=30
if b>a or b<c:
    print('b is greater than a or less than c')
else:
    print('No conditions met')
    
 #fico score
# =============================================================================
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'
# =============================================================================
fico=700
if fico>=300 and fico<400:
    ficocat='Very poor'
elif fico>=400 and fico<600:
    ficocat ='poor'
elif fico>=601 and fico<660:
    ficocat='Fair'
elif fico>=660 and fico <700:
    ficocat='Good'
elif fico>=700:
    ficocat='Excellent'
else:
    ficocat='Unknown'
    print(ficocat)

#For loops
fruits=('apple','pear','banana','cherry')
for x in fruits:
    print(x)
    
for x in range (0,4):
    y=fruits[x]+' for sale'
    print(y)
    
#Applying for loops in loandata

length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x] 
    if category>=300 and category < 400:
        cat = 'Very poor'
    elif category >= 400 and category <600:
        cat='Poor'
    elif category >= 601 and category <660:
        cat = 'Fair'
    elif category >= 660 and category <700:
        cat='Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)
    
    ficocat = pd.series(ficocat)
    loandata['fico.category'] = ficocat
        
#df.loc as conditional statement
#For interest rate, a new column is wanted. If the rate is >0.12 then high else low

loandata.loc[loandata['int.rate']>0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']<=0.12, 'int.rate.type'] = 'Low'
             
loandata['int.rate.type'].describe()
loandata.iloc[:,15]

# Install Matplotlib
#Open anaconda prompt and type: pip install matplotlib
#import matplotlib
import matplotlib.pyplot as plt
#Number of loans/rows by fico category
catplot = loandata.groupby(['fico']).size()
catplot.plot.bar()        
plt.show()   

purposecount=loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red',width=0.2)        
plt.show()

#Scatter Plot
ypoint=loandata['annualincome']
xpoint=loandata['dti']
plt.scatter(xpoint,ypoint, color='green')

# writing loandata to csv
loandata.to_csv('loan_cleaned.csv',index=True)    

loandata.describe()
loandata['int.rate'].describe()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        