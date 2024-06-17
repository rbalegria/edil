import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

st.header("Confirm Your Gender")
sign = Image.open("image/male_and_female.jpg")
st.sidebar.image(sign, caption="Female or Male", width = 100)

height = pd.read_csv("dataset/heights_weights.csv")
height.head()

# Seperate into predictors and predicted
x = height.iloc[:, :-1]
y = height.iloc[:,-1]
x.head()

# Seperate into Train and Test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.3, random_state=42)

# Training the model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='newton-cg')

#Fit to train model
model.fit(x_train, y_train)

# Predicting the y
height = st.number_input("Enter your height in cm")
weight = st.number_input("Enter your weight in lb")
if st.button("Predict"):
    y_predict = model.predict([[height, weight]])
    if y_predict == 1:
        st.write("You are a Male")
        male = Image.open("male_com.jpg")
        st.image(male, width = 550)
    else:
        st.write("You are a Female")
        female = Image.open("Female_com.jpg")
        st.image(female, width = 550)

hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
