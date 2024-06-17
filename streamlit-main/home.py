import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("prediction.py", "Age Group ML Model", "1️⃣", in_section=True),
        Page("analyzer.py", "Basic Sentiment Analyzer", "2️⃣", in_section=True),
        Page("classify.py", "Image Classification", "3️⃣", in_section=True),

        Section("Sample Source Code", "💾"),
        Page("prediction_src.py", "Age group prediction SRC", "1️⃣", in_section=True),
        Page("analyzer_src.py", "Basic Sentiment Analyzer SRC", "2️⃣", in_section=True),
        Page("classify_src.py", "Image Classification SRC", "3️⃣", in_section=True),
    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 ML Learning by [Rhealyn Barrientos Alegria](https://www.facebook.com/rhealyn.alegria.7)")

st.image("./me.jpg")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit")
st.markdown("---")


st.markdown("""
### 👨‍🎓 Read More

##### 👨‍👦‍👦 Description of Apps

* The prediction application is designed to determine a person's gender based on an analysis of their height and weight on the required input in prediction.py file
* The Sentiment Analyzer is a sophisticated tool designed to identify and interpret emotions based on the input provided in the analyzer.py file.
* The image classification tool is designed to identify a person's age group based on the image they upload, utilizing the algorithm implemented in the classify.py file.

##### 👨‍🔧 What I have Learned

Through the development of the Prediction app, Sentiment Analyzer, and Image Classification app using Streamlit,
I have acquired extensive knowledge and practical experience in several critical areas.
This journey has deepened my understanding of various machine learning algorithms and their training processes,
as well as techniques for data cleaning and preparation and evaluating model performance.
Specifically, I have learned how to process and analyze text data for sentiment analysis,
handle and classify image data with machine learning models,
and develop interactive web applications for user-friendly interfaces.
Furthermore, I have significantly enhanced my Python programming skills,
especially in integrating machine learning models into Streamlit apps.
This experience has also provided valuable insights into
project planning, development, and deployment of real-world applications.

### 🔎 Overview""", unsafe_allow_html=True)

st.image("./image/backs.jpg")

st.markdown("""
              My name is Rhealyn B. Alegria, a 21-year-old student from Carlos Hilado Memorial State University,
              currently enrolled in BSIS 3B. I have acquired various skills in programming languages such as HTML & CSS,
              PHP, SQL. Through the development of my applications, I have created a
              Prediction app that uses trained models for forecasting and estimating outcomes, a Sentiment Analyzer that
              determines the sentiment of text data, and an Image Classification app that categorizes images using machine
              learning models. These projects have deepened my understanding of algorithmic processes, data preparation,
              model evaluation, and the deployment of machine learning models in user-friendly interfaces. Additionally, I
              have improved my skills in building interactive applications with Streamlit, furthering my knowledge in both
              programming and machine learning domains.
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
home.py
