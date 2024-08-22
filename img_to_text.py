import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer YOUR KEY"}

def query(file):
    # Directly read the content of the uploaded file
    data = file.read()
    # Send the data to the API
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


st.title("Image Upload and API Query")

# File uploader in Streamlit
uploaded_file = st.file_uploader("Upload an IMAGE", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Send the file to the API and get the response
    response = query(uploaded_file)

    if isinstance(response, list) and "generated_text" in response[0]:
        generated_text = response[0]["generated_text"]
        # Display the text in a single line
        st.write(f"API Response: {generated_text}")
    else:
        st.write("Unexpected response format")
