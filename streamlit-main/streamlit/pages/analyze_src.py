import streamlit as st


st.header('Sentiment Analyzer Source Code')
st.subheader('This python code is implemented for Streamlit')
st.code('''
       import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names


# Set up the title and description
st.title("Castro's Feelings Analyzer :the_horns:")
st.markdown("""
Welcome to Castro's Streamlit app for analyzing different feelings.
Enter your current feeling in the text box below, and let's see what the sentiment analyzer says!
""")

# Input field for user to enter their feeling
message = st.text_input("Tell me what you feel today:")

# Load the trained Naive Bayes classifier from the saved file
model_filename = './pages/CastrosentimentAnalyzerTest_model.sav'
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Define function to extract features from the input message
def word_features(words):
    return {word: True for word in words}

# Function to determine and display the sentiment
def classify_feeling():
    if message:
        message_tone = loaded_model.classify(word_features(message.split()))

        # Determine the sentiment and corresponding emoji
        if message_tone == 'happy':
            st.write("You seem happy! :smile:")
        elif message_tone == 'sad':
            st.write("You seem sad. :pensive:")
        elif message_tone == 'angry':
            st.write("You seem angry. :rage:")
        elif message_tone == 'nervous':
            st.write("You seem nervous. :grimacing:")
        else:
            st.write("Hmm, I'm not sure about that feeling. :thinking_face:")
    else:
        st.write("Please enter a feeling to analyze.")

# Button to trigger the sentiment analysis
st.button('Analyze Feeling', on_click=classify_feeling)

    ''')