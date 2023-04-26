import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
import re
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer() 

def preprocess(sentence):
    
    sentence=str(sentence)
    sentence = sentence.lower()
    sentence=sentence.replace('{html}',"")  #replace html tag
    url_removed=re.sub(r'http\S+', '',sentence) #remove the url
    numbers_removed = re.sub(r'[^a-zA-Z]', ' ', url_removed) #remove the special characters
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(numbers_removed)  
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('english')]
    stem_words=[stemmer.stem(w) for w in filtered_words]
    lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
    return " ".join(lemma_words)

sentence="#$$Yesterday I watched one horror film and it was terrific 232 {html}, http//::dfdf"
cleanText=preprocess(sentence) 
print(cleanText)