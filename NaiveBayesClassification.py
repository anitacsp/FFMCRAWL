import re
import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def normalize(text):
    #put all text to lower
    text = text.lower()
    #remove non-internal punctuations
    text = re.sub('\s\W', ' ', text)
    text = re.sub('\W\s', ' ', text)
    #remove double spaces
    text = re.sub('\s+', ' ', text)

    return text


#retrieve ESG samples & non-ESG samples
esgSample = pd.read_csv(r"C:\Users\chias\source\repos\FFMCRAWL\data files\ESG Dataset.csv")
sample = pd.read_csv(r"C:\Users\chias\source\repos\FFMCRAWL\data files\sample.csv")

#retrieve useful columns with useful data
esgUse = esgSample[['Title', 'ESG', 'neg', 'neu', 'pos', 'compound' ]]
samUse = sample[['Title', 'ESG', 'neg', 'neu', 'pos', 'compound']]

#join both sets of data together
allSample = esgUse.append(samUse)

#normalize all data
allSample['nom'] = [normalize(text) for text in allSample['Title']]

vec = CountVectorizer()
x = vec.fit_transform(allSample['nom'])

encode = LabelEncoder()
y = encode.fit_transform(allSample['ESG'])

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 2)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

baes = MultinomialNB()
baes.fit(x_train,y_train)

y_predicted = baes.predict(x_test)

print(baes.score(x_test, y_test))

print(accuracy_score(y_test, y_predicted))
