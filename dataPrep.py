import pandas as pd
import sentimentAnalysis as SA

class dataPrep:  

    def ESGsent(self, fileLoc):
        df = pd.read_csv(fileLoc)
        print('csv read')
        sentimentCheck = SA.sentimentAnalysis()
        print("sentimentanalysis object created")

        compound = 0
        negCount = 0
        posCount = 0
        neuCount = 0

        for index, row in df.iterrows():
            title = row['Title']
            score = sentimentCheck.analyze(title)
    
            df.loc[index, 'neg'] = score.get('neg')
            df.loc[index, 'neu'] = score.get('neu')
            df.loc[index, 'pos'] = score.get('pos')
            df.loc[index, 'compound'] = score.get('compound')
            compound += score.get('compound')

            if score.get('compound') > 0:
                posCount +=1
            elif  score.get('compound') < 0:
                negCount +=1
            else: 
                neuCount +=1

        print("avg sentiment = " + repr(compound/len(df.index)))
        print('posCount = ' + repr(posCount))
        print('pct pos: ' + repr(posCount*100/len(df.index))) 
        print('negCount = ' + repr(negCount))
        print('pct neg: ' + repr(negCount*100/len(df.index)))
        print('neuCount = '+ repr(neuCount))
        print('pct neu: ' + repr(neuCount*100/len(df.index)))


        df.to_csv(fileLoc, encoding = 'utf-8')

        return len(df)


    def createSample(self, fileLoc, size):
     
        df = pd.read_csv(fileLoc)        
        n = size/len(df.index)
        print(n)
        rand = df.sample(frac=n, random_state=1)
        print(rand.mean(axis=0))

        rand.to_csv("sample.csv", encoding ='utf-8')


    pass

