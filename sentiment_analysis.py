from textblob import TextBlob
import pandas as pd
df=pd.read_csv('review.csv')
df[['polarity', 'subjectivity']] = df['Review'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))

def analysis(score):
    if score < -0.2:
        return 'Negative'
    elif ((score > -0.2) and (score<0.2)):
        return 'Neutral'
    else:
        return 'Positive'
df['Analysis'] = df['polarity'].apply(analysis)


import matplotlib.pyplot as plt  
import seaborn as sns  
#loading the dataset 'tips'  
#plotting the graph  
sns.countplot(x='Analysis',data=df) 
plt.show()  
