
# Face Orientation Classifier

This project is an image classification tool built using Streamlit and Landing.ai's Python SDK. The classifier is designed to determine the orientation of a face in an image, categorizing it as either "Left," "Right," or "Front." The model has been trained using Landing.ai's platform, leveraging advanced deep learning techniques for accurate classification.


## Features
Upload Image: Users can upload a face image to be classified.
Orientation Detection: The classifier determines whether the face in the image is oriented to the left, right, or facing front.
Real-time Feedback: Results are displayed immediately after the image is processed.
## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/face-orientation-classifier.git
cd face-orientation-classifier
```
Install the required packages:
```bash
git clone https://github.com/yourusername/face-orientation-classifier.git
cd face-orientation-classifier
```
Set up Landing.ai API:
Sign up at Landing.ai.
Obtain your API key and model ID from Landing.ai.
Create a .env file in the project directory and add your credentials

```bash
LANDINGAI_API_KEY=your_api_key
LANDINGAI_MODEL_ID=your_model_id
```
Run the application:
```bash
streamlit run app.py
```
## Usage

Upload an Image: Click the "Browse files" button to upload a face image.
View Results: The application will display whether the face is oriented to the left, right, or front