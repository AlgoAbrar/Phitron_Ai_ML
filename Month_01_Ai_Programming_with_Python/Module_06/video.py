import streamlit as st

st.title("Input your video", anchor=False)
st.divider()


#st.video("video/vid1.mp4", loop=True) # From Local

# st.divider()
# From input

video_file = st.file_uploader("Enter Your audio: ", 
                 type=['mp4'])

button= st.button("click to upload")

print(type(video_file))

if button:
    if video_file:
        st.video(video_file)
        st.success("Your file is uploaded successfull")
else:
    st.error("You must upload a video")
    print("no audio file")