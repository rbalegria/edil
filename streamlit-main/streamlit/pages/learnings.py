import streamlit as st
st.set_page_config(layout="wide", page_title="Learnings")

st.title("🧠What I have Learned")
st.header('💭Learnings..!')

st.image("./ml.jpg")

st.markdown("""
#
                Learnings from Quantitative Methods: Building Foundations for the Future:
Quantitative Methods, as a topic, has given me a thorough knowledge of the fundamental skills and procedures necessary
to evaluate and interpret data. This course has helped me get the skills needed for a variety of applications, ranging 
from fundamental data analysis to more complicated jobs such as picture classification and sentiment analysis. 
The information and abilities I learned from this topic are certain to serve as a foundation for my future ambitions.
            
 The skills and knowledge gained from studying Quantitative Methods are not just academic achievements but are practical 
 tools that will enhance my future career. The ability to analyze data, write code, and apply machine learning techniques 
opens up numerous opportunities in various fields. Whether I pursue a career in data science, artificial intelligence, finance, 
healthcare, or any other industry, the foundation built through this course will be instrumental in my success.

Moreover, the interdisciplinary nature of these skills means that I can contribute to innovative projects and solve complex problems
that require a blend of analytical thinking and technical proficiency. The quantitative methods I have learned will enable me to adapt
to new challenges, continuously learn, and stay at the forefront of technological advancements.

The subject of Quantitative Methods has been a transformative learning experience, providing me with essential skills and knowledge that
will be crucial for my future endeavors. From basic coding and data analysis to advanced applications like image classification and 
sentiment analysis, the competencies gained from this course will empower me to make significant contributions in my chosen field and beyond.           
            """, unsafe_allow_html=True)

with st.expander("🔧Practical Applications"):
    st.markdown("""
    
    #
                Image Classification:
One of the exciting applications of the skills learned in Quantitative Methods is image classification. By understanding how to preprocess data,
                train machine learning models, and evaluate their performance, I can develop systems that accurately classify images. For instance, creating an image 
                classification model for identifying different types of flowers—such as roses, sunflowers, lilies, lavenders, and daisies—demonstrates how theoretical
                knowledge can be applied to real-world problems. This skill is particularly relevant in fields like computer vision, agriculture, and environmental monitoring.
                
                Sentiment Analysis:
Another practical application is sentiment analysis, which involves analyzing text data to determine the sentiment behind it—whether it is positive,
                 negative, or neutral. The ability to build sentiment analyzers is immensely useful in areas like market research, customer feedback analysis, and social media
                 monitoring. By combining data analysis techniques with natural language processing (NLP), I can develop tools that help businesses understand customer emotions
                 and improve their products and services accordingly.
    """, unsafe_allow_html=True)