import streamlit as st

st.title("Input your files", anchor=False)
st.divider()

image1 = st.file_uploader("Enter Your Image: ", 
                 type=['jpg','jpeg','png'])

print(type(image1))

if image1:
    st.image(image1)
else:
    st.write("No Image Uploaded")
