import streamlit as st

st.title("AI Note Summary and Quiz Generator",anchor=False)
st.markdown("Upload max 3 photos")
st.divider()

# Sidebar
with st.sidebar:
    #image works
    st.header("Controls")
    images= st.file_uploader("Upload Images:",
                     type=['jpg','jpeg','png'],
                     accept_multiple_files=True
                     )
    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            col= st.columns(len(images))
            
            st.subheader("Your Uploaded Images")
            
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    # Difficulty Select
    selected_option= st.selectbox("Enter the Difficulty of your Quiz",
                 ("Easy", "Medium", "Hard"),
                 index=None
                 )
    if selected_option:
        st.markdown(f"You selected ***{selected_option}*** as Difficulty")
    else:
        st.error("Select a difficulty")
    button= st.button("Click for Magic", type="primary")
    
    
    