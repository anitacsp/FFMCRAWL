import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

esgSample = pd.read_csv(r"C:\Users\chias\source\repos\FFMCRAWL\data files\ESG Dataset.csv")
sample = pd.read_csv(r"C:\Users\chias\source\repos\FFMCRAWL\data files\sample.csv")

print(esgSample.head())
print(sample.head())
