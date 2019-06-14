import re
import numpy as np
import pandas as pd
import csv
import nltk
import time
from nltk.corpus import stopwords

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

start = time.time()
#retrieve ESG samples & non-ESG samples
esgTrain = pd.read_csv(r"C:\Users\chias\source\repos\FFMCRAWL\data files\ESG Dataset.csv")
noesgTrain = pd.read_csv(r"C:\Users\chias\source\repos\FFMCRAWL\data files\sample.csv")
print("Training dataset imported")

etTest = pd.read_csv(r"C:\Users\chias\source\repos\FFMCRAWL\bbg.csv")
print("Testing dataset imported")



#retrieve useful columns with useful data
esgUse = esgTrain[['Title', 'ESG', 'compound' ]]
samUse = noesgTrain[['Title', 'ESG', 'compound']]
etUse = etTest[['Title', 'compound', 'Link to article']]

#join both sets of data together
allSample = esgUse.append(samUse)


#normalize all title
allSample['nom'] = [normalize(text) for text in allSample['Title']]
allSample['id'] = np.arange(len(allSample))
allSample.set_index('id', inplace=True)
print("Training dataset normalized")

etUse['nom'] = [normalize(text) for text in etUse['Title']]
etUse['id'] = np.arange(len(etUse))
etUse.set_index('id', inplace=True)
print("Testing dataset normalized")


stopWords = set(stopwords.words('english'))
allSample['nom'] = allSample['nom'].apply(lambda x: ' '.join([item for item in x.split() if item not in stopWords]))
print("Training stopwords removed")

etUse['nom'] = etUse['nom'].apply(lambda x: ' '.join([item for item in x.split() if item not in stopWords]))
print("Testing stopwords removed")


#transform text data to vectors
vec = CountVectorizer()
x =vec.fit_transform(allSample['nom'])
print("Training data vectorized")

test = vec.transform(etUse['nom'])
print("Testing data vectorized")


#split into train & test datasets
x_train, x_test, y_train, y_test = train_test_split(x,allSample['ESG'], test_size = 0.2, random_state=1)
x_train = x
y_train = allSample['ESG']
x_test = test
print(x_train.shape)
print(x_test.shape)

#Naive Bayes model chosen. Light weight
baes = MultinomialNB()
#training our model
baes.fit(x_train,y_train)

#Print accuracy no. of rights/total results
#print(baes.score(x_test, y_test))
#Prints confusion matrix: postive, false postive, negative, false negative
#print(confusion_matrix(y_test,baes.predict(x_test), labels = [0,1]))

#Preparing dataset to be exported to csv
output = pd.DataFrame(data=etUse)

output['pred'] = baes.predict(x_test)

print(list(output))
usableData = output[[ 'Title', 'compound', 'pred', 'Link to article']]
usableData.to_csv('bbgOutput.csv')

end = time.time() - start
print("Total time taken: "+ str(end))