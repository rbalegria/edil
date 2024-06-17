
from PIL import Image
from io import BytesIO
import streamlit as st
import pickle
from img2vec_pytorch import Img2Vec

with open('random_forest_model.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()

## Streamlit Web App Interface
st.set_page_config(layout="wide", page_title="Image Classification for age group")

st.write("## This is a demo of an age group Image Classification Model in Python!")
st.write(
    ":grin: We'll try to predict the image on what features it was trained via the uploaded image :grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image
@st.cache(allow_output_mutation=True)
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="jpeg")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    col1.write("Image to be predicted :camera:")
    col1.image(image)

    col2.write("Category :wrench:")
    img = Image.open(upload).convert('RGB')  # Ensure image is in RGB format
    features = img2vec.get_vec(img)
    print("Features:", features)  # Debugging: Print features
    pred = model.predict([features])
    print("Prediction:", pred)  # Debugging: Print prediction
    col2.header(pred)


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    st.write("by koalatech...")

