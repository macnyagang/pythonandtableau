# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:31:41 2024

@author: nyangang
"""
# Reading excel or xlsx files
import pandas as pd
data=pd.read_excel('articles.xlsx')

#Summary of columns
data.describe()
data.info()

#Counting the number of articles per source
#format of groupby: df.groupby(['column_to_group'])['column_to_count'].count()
data.groupby(['source_id'])['article_id'].count()

#Number of reactions per publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#Dropping a column
data=data.drop('engagement_reaction_count', axis=1)

#Functions tracking keywords in articles
def thisfunction():
    print('This is my first function')
# Call the function
thisfunction()

# Creating keyword function

def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0, length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
keywordflag = keywordflag('murder')


 
    
    
def aboutMe(name, surname, location):
    print('This is ' + name + '. My surname is ' + surname + '. I am from ' + location + '.')
    a = aboutMe('Dee', 'Naidoo', 'South Africa')
    return name, surname, location
    
#Playing around with Classes

class Car:
    type = 'Automobile'# class attribute
    def __init__(self,name, make, color):
        self.carname = name # instance attributes
        self.carmake = make # instance attributes
        self.carcolor = color #instance 
mycar = Car('gclass','mercedes','black')

 
 # Sentiment Analysis in blogme
 # The us e of vader sentiments
 # Install vaderlibrary in python
 # Sentiment Intensity Analyzer
 
 from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
 sent_int = SentimentIntensityAnalyzer()
 text = data['title'][15]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#Use for loop to extract sentiments for title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)
for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg= sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

# Create columns in dataframe

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment
    
#Writing or saving the data to excel
data.to_excel('blogme_clean.xlsx',sheet_name = 'blogme_data', index = False)
    
    
    
    
    
    
    
    
    
    