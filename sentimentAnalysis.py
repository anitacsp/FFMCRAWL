#@gaybirdy
# Evaluates the sentiment of a given title based on 
# VADER's sentiment intensity analyzer
# http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf

import nltk
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class sentimentAnalysis:

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, sentence):
        #print(sentence)
        #print(type(sentence))
        score = self.analyzer.polarity_scores(sentence)
         
        return score

#{'neg': 0.231, 'neu': 0.769, 'pos': 0.0, 'compound': -0.34}
    def prettyRow(self, title, score, url):
        row =[title]

        compound = score.get('compound')
        row.append(compound)
        
        sent = 2
        if compound <= -0.6:
            sent =-2
        elif compound <= -0.2:
            sent = -1
        elif compound < 0.2:
            sent = 0
        elif compound <= 0.6:
            sent = 1

        row.append(sent)
        row.append(url)
        return row
        

    pass




