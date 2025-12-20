import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import cv2
IMG_SIZE = 128
model = load_model("my_image_model_deployment.h5")
labels = ["Benign", "Malignant"]
thresholds = {"Benign": 0.5, "Malignant": 0.65}
def preprocess_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)
    return img
def predict_image(img):
    img = preprocess_image(img)
    preds = model.predict(img)[0]
    class_idx = np.argmax(preds)
    confidence = preds[class_idx]
    predicted_label = labels[class_idx]

    if predicted_label == "Benign" and confidence < thresholds["Benign"]:
        st.warning(f"Confidence for Benign ({confidence*100:.2f}%) below 50%, switching to Malignant")
        class_idx = 1
        confidence = preds[class_idx]
    elif predicted_label == "Malignant" and confidence < thresholds["Malignant"]:
        st.warning(f"Confidence for Malignant ({confidence*100:.2f}%) below 65%, switching to Benign")
        class_idx = 0
        confidence = preds[class_idx]
    return labels[class_idx], confidence
st.title("Image Classification Web App")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.image(img, channels="RGB", caption="Uploaded Image")
    pred, conf = predict_image(img)
    st.success(f"Prediction: {pred}")
    st.info(f"Confidence: {conf*100:.2f}%")
