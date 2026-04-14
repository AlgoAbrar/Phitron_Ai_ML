import streamlit as st

st.title("Input your files", anchor=False)
st.divider()


st.audio("audio/aud1.mp3", loop=True) # From Local

st.divider()
# From input

audio_file = st.file_uploader("Enter Your audio: ", 
                 type=['mp3','ogg','flac'])

print(type(audio_file))

if audio_file:
    st.audio(audio_file)
else:
    print("no audio file")