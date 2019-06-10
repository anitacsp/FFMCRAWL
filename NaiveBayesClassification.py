import re
import numpy as np
import pandas as pd
import csv

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

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
allSample['id'] = np.arange(len(allSample))

#normalize all title
allSample['nom'] = [normalize(text) for text in allSample['Title']]
allSample.set_index('id', inplace=True)

#transform text data to vectors
vec = CountVectorizer()
#allSample['x'] = vec.fit_transform(allSample['nom'])
x =vec.fit_transform(allSample['nom'])
#cat.to_csv("test.csv", encoding ='utf-8')

#encode = LabelEncoder()
#y = encode.fit_transform(allSample['ESG'])
#allSample['y-axis'] = allSample['ESG']

#split into train & test datasets
x_train, x_test, y_train, y_test = train_test_split(x,allSample['ESG'], test_size = 0.2, random_state=1)

baes = MultinomialNB()
baes.fit(x_train,y_train)
#baes.score(x_test, y_test)
print(baes.score(x_test, y_test))
print(confusion_matrix(y_test,baes.predict(x_test), labels = [0,1]))

sub = pd.DataFrame(data=y_test)
sub['pred'] = baes.predict(x_test)

output = pd.merge(allSample, sub, on = 'id')


usableData = output[['Title','compound', 'ESG_x', 'pred']]
usableData.to_csv('out2.csv')