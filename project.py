import streamlit as st
from PIL import Image
from landingai.predict import Predictor

# Streamlit App Title
st.title("Image Prediction with LandingAI")

# API Configuration
endpoint_id = "b467bbb7-8099-4b5a-9b4e-1bbc9a7b5edb"
api_key = "land_sk_3vpwerFRLEzDuTPlkyx3FvK5FjrsIBeXfasnxla6aSa3a5GLAH"

# Function to Load and Predict Image
def load_image(image_file):
    img = Image.open(image_file)
    return img

def predict_image(image):
    predictor = Predictor(endpoint_id, api_key=api_key)
    predictions = predictor.predict(image)
    return predictions

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Load and predict
    img = load_image(uploaded_file)
    predictions = predict_image(img)

    # Display the predictions
    st.write("Predictions:")
    st.json(predictions)
