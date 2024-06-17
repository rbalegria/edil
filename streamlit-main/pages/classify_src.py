import streamlit as st


st.header('Image Classification App')
st.subheader('This model was trained using a dataset')
st.code('''

import os
import pickle
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from img2vec_pytorch import Img2Vec  # Import img2vec_pytorch module
import streamlit as st  # Import Streamlit library

data_dir = './dataset'
train_dir = os.path.join(data_dir, 'train')
val_dir = os.path.join(data_dir, 'val')

# Create an instance of Img2Vec
img2vec = Img2Vec()

data = {}
for j, dir_ in enumerate([train_dir, val_dir]):
    features = []
    labels = []
    for category in os.listdir(dir_):
        category_dir = os.path.join(dir_, category)
        if not os.path.isdir(category_dir):
            continue  # Skip non-directory items

        for img_path in os.listdir(category_dir):
            img_path_ = os.path.join(category_dir, img_path)
            if not os.path.isfile(img_path_):
                continue  # Skip non-file items

            img = Image.open(img_path_).convert('RGB')

            img_features = img2vec.get_vec(img)

            features.append(img_features)
            labels.append(category)

    data[['training_data', 'validation_data'][j]] = features
    data[['training_labels', 'validation_labels'][j]] = labels

# train model
model = RandomForestClassifier(random_state=0)
model.fit(data['training_data'], data['training_labels'])

# test performance
y_pred = model.predict(data['validation_data'])
score = accuracy_score(y_pred, data['validation_labels'])

print(score)

# Save the trained model to a file
with open('random_forest_model.p', 'wb') as file:
    pickle.dump(model, file)

print("Model saved as 'random_forest_model.p'")

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
''')
