import streamlit as st

st.title("Input your files", anchor=False)
st.divider()

image1 = st.file_uploader("Enter Your Image: (at max 2) ", 
                 type=['jpg','jpeg','png'],
                 accept_multiple_files=True)

print(type(image1))

# if image1:
#     st.image(image1)
# else:
#     st.write("No Image Uploaded")


# in a column side by side
if image1:
    if(len(image1)>2):
        st.warning("You uploaded more than 2 photos")
    else:
        col = st.columns(len(image1)) # column object akare banabe
    
        for i,per_image in enumerate(image1):
            with col[i]:
                st.image(per_image)
            

else:
    st.write("No Image Uploaded")
    #internal image
    #st.image("images/img1.jpg") # we can also add web url