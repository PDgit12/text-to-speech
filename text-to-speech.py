import streamlit as st
from gtts import gTTS
import io
from PIL import Image

def main():
    st.set_page_config(
        page_title="Text-to-Speech App",
        page_icon="🔊",
        layout="wide"
    )

    st.title("🔊 Speak It Out! - Text-to-Speech App")
    st.write("Type in your text, and let us speak it aloud for you!")

    user_input = st.text_area("Enter text here", height=150)

    if st.button("Speak"):
        if user_input:
            st.write("You entered:")
            st.write(user_input)

            tts = gTTS(user_input)
            audio = io.BytesIO()
            tts.save(audio)

            st.audio(audio.getvalue(), format="audio/mp3")

    st.write("---")
    st.write("Built with ❤️ by [Your Name]")
    st.write("Have suggestions? Reach out to me at [Your Contact Info]")

if __name__ == "__main__":
    main()

