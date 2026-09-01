### Health Management APP
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini 3.6 Flash and get response
def get_gemini_response(input_text, image_parts, prompt):
    model = genai.GenerativeModel("gemini-3.5-flash-lite")

    # Use Interactions API style
    response = model.generate_content(
        contents=[
            {"role": "user", "parts": [input_text]},
            {"role": "user", "parts": image_parts},
            {"role": "user", "parts": [prompt]}
        ]
    )

    return response.text

# Function to prepare image input
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me the total calories")

# Nutrition prompt
input_prompt = """
You are an expert nutritionist. Look at the food items in the image
and calculate the total calories. Also provide details of each food item
with its calorie intake in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
---
Total Calories: XYZ
"""

# If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input_text)
    st.subheader("The Response is")
    st.write(response)
