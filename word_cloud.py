#Wordcloud
from stop_words import get_stop_words
import re
import nltk
from matplotlib import pyplot as plt 
import seaborn as sns
from nltk.tokenize import word_tokenize
import pandas as pd

top_200 = 200

#Read the data
data=pd.read_csv('review.csv')
lower_data = data['Review'].str.lower().str.cat(sep=' ') #Concatenate

# removes punctuation,numbers
data_list = re.sub('[^A-Za-z0-9]', ' ', lower_data)

#remove the stopwords
stop_words = list(get_stop_words('english'))
word_tokens = word_tokenize(data_list)
filtered_sentence = []
for word in word_tokens:
    if word not in stop_words:
        filtered_sentence.append(word) 
     
#remove stopwords based on Custom stopwords
stopwordlist = ['movie', 'film','one','really','just','can']
finalList=[]
for j in filtered_sentence:
    if j not in stopwordlist:
        finalList.append(j)
           
# Remove characters which have length less than 2  
without_single_chr = [word for word in finalList if len(word) > 2]

# Calculate frequency distribution
word_dist = nltk.FreqDist(without_single_chr)
#choose top 200 words 
result = pd.DataFrame(word_dist.most_common(top_200), columns=['Word', 'Frequency'])
#plot
plt.figure(figsize=(12,8))
sns.set_style("whitegrid")
ax = sns.barplot(x="Word",y="Frequency", data=result.head(20))

