import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from sklearn.base import BaseEstimator, TransformerMixin

nltk.download('stopwords')
nltk.download('wordnet')

stopwords = set(stopwords.words('english'))
lemetizer = WordNetLemmatizer()

class Preprocessing(BaseEstimator, TransformerMixin) :
    def fit(self, x, y):
        return self

    def healper(self, x):
        data = re.sub(r'[^a-zA-z\s]','',x.lower())

        data = data.split()

        cleaned = [w for w in data if w not in stopwords]

        cleaned = [lemetizer.lemmatize(w) for w in cleaned]

        return ' '.join(cleaned)

    def transform(self, x):

        combined = x['Headline'] + ' ' + x['Content']

        return combined.apply(self.healper)
