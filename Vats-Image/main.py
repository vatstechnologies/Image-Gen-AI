import streamlit as st
from transformers import pipeline
import requests
from PIL import Image
import pyttsx3
import io

# Initialize Hugging Face text generation pipeline
generator = pipeline("text-generation", model="gpt2")  # You can replace "gpt2" with other models

# Streamlit App Title
st.title("🖼️✨ VatsGenix.AI - Personalized Image & Text Generator")

# Sidebar for Navigation
st.sidebar.title("🔍 Select Mode")
option = st.sidebar.radio("Choose an AI Task:", ["Generate Text", "Generate Image", "Text-to-Speech"])

### ========================== TEXT GENERATION ============================
if option == "Generate Text":
    st.subheader("📝 AI-Powered Text Generation")
    user_input = st.text_area("Anurag's AI Is waiting for your Prompt:", "Write a futuristic story about AI.")

    if st.button("Generate Text"):
        if user_input:
            with st.spinner("Generating text..."):
                try:
                    # Generate text using Hugging Face's GPT-2 (or other available models)
                    generated_text = generator(user_input, max_length=500, num_return_sequences=1)[0]["generated_text"]
                    st.success("✅ Successfully generated!")
                    st.write(generated_text)
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

### ========================== IMAGE GENERATION ============================
elif option == "Generate Image":
    st.subheader("🖼️ AI-Powered Image Generation")
    img_prompt = st.text_area("Enter an image description:", "Image Generation Is In Progress !")

    if st.button("Generate Image"):
        if img_prompt:
            with st.spinner("Generating image..."):
                try:
                    # Use OpenAI or Hugging Face for image generation (OpenAI is an example here)
                    # You can replace this with any image generation API or Hugging Face model
                    response = requests.post(
                        "https://api.openai.com/v1/images/generations",
                        headers={"Authorization": f"Bearer YOUR_OPENAI_API_KEY"},
                        json={"prompt": img_prompt, "n": 1, "size": "1024x1024"}
                    )
                    image_url = response.json()['data'][0]['url']
                    image_response = requests.get(image_url)
                    img = Image.open(io.BytesIO(image_response.content))
                    st.image(img, caption="Generated Image")
                    st.success("✅ Successfully generated image!")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

### ========================== TEXT-TO-SPEECH ============================
elif option == "Text-to-Speech":
    st.subheader("🔊 AI-Powered Text-to-Speech")
    tts_text = st.text_area("Enter text to convert into speech:", "TTS Is In Progress !!")

    if st.button("Convert to Speech"):
        if tts_text:
            with st.spinner("Converting to speech..."):
                try:
                    # Convert text to speech using pyttsx3 (offline, works without API)
                    engine = pyttsx3.init()
                    engine.save_to_file(tts_text, 'output.mp3')
                    engine.runAndWait()

                    # Play the audio file using Streamlit
                    st.audio('output.mp3', format="audio/mp3")
                    st.success("✅ Successfully generated speech!")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

# Footer
st.markdown("🚀 Developed by **VatsGenix AI**")
