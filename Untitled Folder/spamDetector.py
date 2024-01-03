import pickle
import streamlit as st
model=pickle.load(open("spam2.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))


def main():
    st.title("Email Spam Detector Apps")

    main()
