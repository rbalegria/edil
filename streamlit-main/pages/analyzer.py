import streamlit as st
import requests
import pandas as pd
import pickle
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from io import BytesIO
import random
import nltk

# Download the necessary NLTK data
nltk.download('punkt')

@st.cache_data(ttl=60*60*12)
def fetch_emojis():
    resp = requests.get(
        'https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json')
    json = resp.json()
    codes, emojis = zip(*json.items())
    return pd.DataFrame({
        'Emojis': emojis,
        'Shortcodes': [f':{code}:' for code in codes],
    })

def word_features(words):
    return dict([(word, True) for word in words])

def main():
    st.title("Sentiment Analyzer & Emoji Viewer")

    sentence = st.text_input("Enter a sentence to analyze sentiment:")
    analyze_sentiment = st.button("Analyze Sentiment")

    if analyze_sentiment and sentence:
        emotions = {
            'happy': ['joyful', 'content', 'delighted', 'cheerful', 'elated', 'ecstatic', 'gleeful', 'jubilant', 'happy'],
            'sad': ['gloomy', 'melancholic', 'sorrowful', 'depressed', 'mournful', 'grieving', 'despairing', 'down', 'dejected', 'blue', 'sad'],
            'angry': ['furious', 'outraged', 'livid', 'wrathful', 'irritated', 'agitated', 'fuming', 'incensed', 'seething', 'infuriated', 'angry'],
            'excited': ['thrilled', 'eager', 'enthusiastic', 'pumped', 'overjoyed', 'animated', 'ecstatic', 'elated', 'jubilant', 'electrified', 'excited'],
            'nervous': ['anxious', 'worried', 'tense', 'uneasy', 'restless', 'apprehensive', 'trembling', 'fidgety', 'nervous'],
            'scared': ['afraid', 'terrified', 'frightened', 'panicked', 'petrified', 'spooked', 'nervous', 'startled', 'scared']
        }

        emoji_map = {
            'happy': '😊',
            'sad': '😢',
            'angry': '😠',
            'excited': '😃',
            'nervous': '😰',
            'scared': '😱'
        }

        gif_map = {
            'happy': ['https://media.giphy.com/media/1BcfiGlOGXzQ0/giphy.gif', 'https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif'],
            'sad': ['https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif', 'https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif'],
            'angry': ['https://media.giphy.com/media/cm1qLKlYwD01G/giphy.gif', 'https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif'],
            'excited': ['https://media.giphy.com/media/l0ExdMHUDKteztyfe/giphy.gif', 'https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif'],
            'nervous': ['https://media.giphy.com/media/d10dMmzqCYqQ0/giphy.gif', 'https://media.giphy.com/media/3oKIPtjElfqwMOTbH2/giphy.gif'],
            'scared': ['https://media.giphy.com/media/xT9IgB8zEWeGQ2fAmE/giphy.gif', 'https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif']
        }

        train_set = [(word_features(word_tokenize(word)), emotion)
                     for emotion, words in emotions.items()
                     for word in words]

        classifier = NaiveBayesClassifier.train(train_set)

        # Classify and get probabilities
        prob_dist = classifier.prob_classify(word_features(word_tokenize(sentence)))
        sentiment = prob_dist.max()
        probability = prob_dist.prob(sentiment)

        st.write(f"Sentiment: {sentiment}")
        st.write(f"Probability: {probability:.2f}")
        st.write(f"Confidence: {probability * 100:.2f}%")

        # Display analytical report
        st.markdown("## Analytical Report")
        for label in prob_dist.samples():
            st.write(f"{label}: {prob_dist.prob(label):.2f}")

        # Display corresponding emoji and GIF
        st.markdown(f"### {emoji_map[sentiment]}")
        st.image(random.choice(gif_map[sentiment]))

        # Saving the model to a pickle file
        model_bytes = BytesIO()
        pickle.dump(classifier, model_bytes)
        model_bytes.seek(0)

        with open("sentiment_classifier.pickle", "wb") as f:
            f.write(model_bytes.read())
            st.success("Model saved successfully as 'sentiment_classifier.pickle'")

if __name__ == "__main__":
    main()
