import pandas as pd
import sentimentAnalysis as SA
import dataPrep as dp

prep = dp.dataPrep()

sampleSize = prep.ESGsent(r"C:\Users\chias\source\repos\FFMCRAWL\data files\ESG Dataset.csv") 

prep.createSample(r"C:\Users\chias\source\repos\FFMCRAWL\data files\wsjSentiment.csv",sampleSize)