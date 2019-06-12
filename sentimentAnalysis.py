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

        for i in score:
            row.append(score.get(i))
        
        row.append(url)
        return row
        

    pass




