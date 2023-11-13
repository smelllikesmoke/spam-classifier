import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [char for char in text if char not in string.punctuation]
    text = [word for word in text if word not in stopwords.words('english')]
    stemmer = PorterStemmer()
    text = [stemmer.stem(word) for word in text]
    lemmatizer = WordNetLemmatizer()
    text = [lemmatizer.lemmatize(word) for word in text]
    text = ' '.join(text)
    return text

def generate_vectors(text):
    text = [text]
    text = tfidf.transform(text).toarray()
    return text

def predict(text):
    text = transform_text(text)
    text = generate_vectors(text)
    prediction = model.predict(text)
    return prediction

def display_result(prediction):
    if prediction == 0:
        st.write("Not Spam")
    else:
        st.write("Spam")

st.title("Sentiment Analysis using Machine Learning")
st.subheader("Enter the text to check the sentiment")

review = st.text_area("Enter the text")
if st.button("Predict"):
    review = transform_text(review)
    review = tfidf.transform([review]).toarray()
    prediction = model.predict(review)[0]

    if prediction == 0:
        st.write("Not Spam")
    else:
        st.write("Spam")
