import streamlit as st

st.title("AI Note Summary and Quiz Generator",anchor=False)
st.markdown("Upload max 3 photos")
st.divider()

# Sidebar section
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
    st.markdown(f"You selected ***{selected_option}*** as Difficulty")
    # if selected_option:
    #     st.markdown(f"You selected ***{selected_option}*** as Difficulty")
    # else:
    #     st.error("Select a difficulty")
    pressed_button= st.button("Click for Magic", type="primary")
    
    
if pressed_button:
    if not images:
        st.error("Please Upload Images")
    if not selected_option:
        st.error("You must select a Difficulty")
    if images and selected_option:
        #note
        with st.container(border=True):
            st.subheader("Your Note",anchor=False)
            # portion below will be replaced by Ai  
            st.text("Note will be shown Here")
            
        # Audio
        with st.container(border=True):
            st.subheader("Audio Explaination",anchor=False)
            # portion below will be replaced by Ai  
            st.text("Note will be shown Here")
        
        # Quiz
        with st.container(border=True):
            st.subheader("Let's Have a Test",anchor=False)
            st.markdown(f"You selected ***{selected_option}*** as Difficulty")
            # portion below will be replaced by Ai  
            st.text("Note will be shown Here")
        
else:
    pass