import streamlit as st

st.title("About Alegria ")



st.title("🖼️Self Gallery")


image_paths = ["./pic/me.jpg",]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨Alegria, Rhealyn B..")

st.markdown("""
##### 👨‍👦‍👦 Family Members

* 🤱 Mother's Name: Alegria, Rolan 
* 👨 Father's Name: Alegria, Lorena
* 👧 Sister's Name: Alegria, Rolyn

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal Information
st.header("Personal Information")
st.write("**Name:** Alegria,Rhealyn B.")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Zone 10, Talisay City")

with st.expander("Who am I 10 years From now??"):
    st.markdown("""
    
    #
                Ten years from now, after graduating college, 
                I envision myself established in a career that aligns with my passions in technology. 
                By then, I aim to have advanced to more senior roles, gaining valuable experience and possibly even starting 
                my own venture or leading impactful projects. Personally, I expect to have a deeper understanding of myself, 
                strong relationships, and a fulfilling balance between work and personal life. Overall, I see myself as a confident, 
                experienced individual making a positive impact and enjoying both professional success and personal growth.

            My Vision
 I aim to apply the skills that I learned from college in real-world scenarios, 
 helping businesses and organizations operate more efficiently and effectively. 
 Beyond technical expertise, I envision developing strong problem-solving abilities and a knack for innovation. 
 Ultimately, I aspire to contribute meaningfully to the digital transformation of industries, 
 making a positive impact on how information is utilized and shared globally.


as an information systems professional, I envision leveraging technical expertise 
to drive innovation and enhance organizational efficiency. 
Contributing to the digital transformation of industries, my goal is to make a positive impact 
on how information is managed and utilized globally.
    """, unsafe_allow_html=True)
# Quotes
st.header("Favorite Quotes")
st.write("1. \"Every day may not be a best day but there is always something good in everyday.\"")
st.write("2. \"Calm seas do not create skilled sailors.\"")
st.write("3. \"Do not lean on your own understanding.\"")
st.write("4. \"Don't be pushed around by the fears in your mind. Be led by the dreams in your heart..\"")
st.write("5. \"Prepare!.\"")




import streamlit as st


images = [
    {"path": "./pic/us1.jpg", "caption": "Throughout my academic journey, the invaluable support of my classmates has been instrumental in shaping my growth and success. As I reflect on the myriad experiences shared with these individuals, it becomes evident that their contributions have enriched my learning, inspired me to persevere through challenges, and fostered a sense of camaraderie that transcends the classroom."},
]


st.title("🖼️Gallery")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: gray;
        padding: 2em;
    }
    h1, h2 {
        color: #4CAF50;
    }
    .stText {
        font-size: 1.2em;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")
