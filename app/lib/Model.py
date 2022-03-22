from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
import spacy
import string
from nltk.corpus import stopwords
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class Model:

    def __init__(self):
        with open('tok.data', 'rb') as doc:
            self.vectorization = pickle.load(doc)

        with open('LR.data', 'rb') as doc:
            self.modelLR = pickle.load(doc)

    def predict(self, data):
        return self.modelLR.predict(data)

    def vectorizer(self, data):
        vec = self.vectorization.transform([data])
        return vec

    @staticmethod
    def clean_data(text):
        nlp = spacy.load('fr_core_news_sm')
        text = text.lower()
        # retirer le saut de ligne
        text = text.replace('\n', ' ')
        text = text.replace("'", ' ')
        new_text = ''
        # retirer la ponctuation
        for char in text:
            if char in string.punctuation or char.isdigit():
                new_text += ' '
            else:
                new_text += char

        # FORME CANONIQUE
        tokens = []
        tokens_texte = nlp(new_text)
        for token in tokens_texte:
            tokens.append(token.lemma_)
        new_text = " ".join(tokens)
        clean_text = []
        # retirer les stops words
        for word in new_text.split(' '):
            if word not in stopwords.words('french') and word not in list(fr_stop) and word != '' and len(word) > 2:
                clean_text.append(word)
        clean_text = " ".join(clean_text)
        return "".join(clean_text)
