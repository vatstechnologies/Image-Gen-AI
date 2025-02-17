import streamlit as st
from transformers import pipeline
from TTS.api import TTS

# Initialize Hugging Face pipeline for image generation (Stable Diffusion)
image_generator = pipeline("text-to-image", model="CompVis/stable-diffusion-v-1-4-original")

# Initialize the TTS model (Coqui TTS)
tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")

# Streamlit UI and functionality
st.title("🖼️✨ VatsGenix - AI Image & Text Generator")

# Sidebar for navigation
st.sidebar.title("🔍 Select Mode")
option = st.sidebar.radio("Choose an AI Task:", ["Generate Text", "Generate Image", "Text-to-Speech"])

# Text Generation Section (Optional, you can update this with your model)
if option == "Generate Text":
    st.subheader("📝 AI-Powered Text Generation")
    user_input = st.text_area("Enter your prompt:", "Write a futuristic story about AI.")
    if st.button("Generate Text"):
        if user_input:
            st.write("Generated text will appear here")

# Image Generation Section (Hugging Face)
elif option == "Generate Image":
    st.subheader("🖼️ AI-Powered Image Generation")
    img_prompt = st.text_area("Enter an image description:", "A futuristic cyberpunk city at night.")
    if st.button("Generate Image"):
        if img_prompt:
            with st.spinner("Generating image..."):
                try:
                    generated_images = image_generator(img_prompt, num_inference_steps=50)
                    st.image(generated_images[0]['image'], caption="Generated Image")
                    st.success("✅ Successfully generated image!")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

# Text-to-Speech Section (Coqui TTS)
elif option == "Text-to-Speech":
    st.subheader("🔊 AI-Powered Text-to-Speech")
    tts_text = st.text_area("Enter text to convert into speech:", "Hello, this is an AI-generated voice.")
    if st.button("Convert to Speech"):
        if tts_text:
            with st.spinner("Converting to speech..."):
                try:
                    audio_path = tts.tts_to_file(tts_text, "output.wav")
                    st.audio(audio_path, format="audio/wav")
                    st.success("✅ Successfully generated speech!")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
