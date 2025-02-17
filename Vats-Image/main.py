import subprocess
import sys

# Function to install missing packages dynamically
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Attempting to import the required libraries, and installing them if not present
try:
    import streamlit as st
except ImportError:
    install("streamlit")

try:
    import torch
except ImportError:
    install("torch")

try:
    from PIL import Image
except ImportError:
    install("Pillow")

try:
    from transformers import pipeline
except ImportError:
    install("transformers")

try:
    import pyttsx3
except ImportError:
    install("pyttsx3")

# Now, proceed with the rest of your code
from transformers import pipeline

# Streamlit app title
st.title("🖼️✨ VatsGenix - AI Image & Text Generator")

# Sidebar for navigation
st.sidebar.title("🔍 Select Mode")
option = st.sidebar.radio("Choose an AI Task:", ["Generate Text", "Generate Image", "Text-to-Speech"])

# ========================== TEXT GENERATION USING HUGGING FACE ============================
if option == "Generate Text":
    st.subheader("📝 AI-Powered Text Generation")
    user_input = st.text_area("Enter your prompt:", "Write a futuristic story about AI.")

    if st.button("Generate Text"):
        if user_input:
            with st.spinner("Generating text..."):
                try:
                    # Use Hugging Face's GPT-2 or GPT-Neo model for text generation (free models)
                    generator = pipeline('text-generation', model='gpt2')
                    generated_text = generator(user_input, max_length=500, num_return_sequences=1)
                    st.success("✅ Successfully generated!")
                    st.write(generated_text[0]['generated_text'])
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

# ========================== IMAGE GENERATION USING HUGGING FACE ============================
elif option == "Generate Image":
    st.subheader("🖼️ AI-Powered Image Generation")
    img_prompt = st.text_area("Enter an image description:", "A futuristic cyberpunk city at night.")

    if st.button("Generate Image"):
        if img_prompt:
            with st.spinner("Generating image..."):
                try:
                    # Using Hugging Face's stable-diffusion model for image generation
                    generator = pipeline('image-generation', model='CompVis/stable-diffusion-v-1-4-original')
                    image = generator(img_prompt)[0]
                    st.image(image, caption="Generated Image")
                    st.success("✅ Successfully generated!")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

# ========================== TEXT-TO-SPEECH USING pyttsx3 ============================
elif option == "Text-to-Speech":
    st.subheader("🔊 AI-Powered Text-to-Speech")
    tts_text = st.text_area("Enter text to convert into speech:", "Hello, this is an AI-generated voice.")

    if st.button("Convert to Speech"):
        if tts_text:
            with st.spinner("Converting to speech..."):
                try:
                    # Using pyttsx3 for offline Text-to-Speech
                    engine = pyttsx3.init()
                    engine.say(tts_text)
                    engine.runAndWait()
                    st.success("✅ Successfully generated speech!")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

# Footer
st.markdown("🚀 Developed by **VatsGenix AI**")
