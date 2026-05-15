from gtts import gTTS
import streamlit as st
import io

text = "Hello, welcome to the course"

speech= gTTS(text,lang='en', slow=False)

# speech.save("Welcome.mp3") #locally save hoye then run hobe. but we have to deploy it.

# Ram er moddhe buffer korte hoi

audio_buffer= io.BytesIO()
speech.write_to_fp(audio_buffer)


#st.audio("welcome.mp3")
st.audio(audio_buffer)