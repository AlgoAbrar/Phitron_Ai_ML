import streamlit as st

st.title("Input your Information", anchor=False)
st.divider()

name= st.text_input("Enter Your Name")

print(type(name))

#st.write("Your name is: ", name)


# Number Input

st.divider()

age = st.number_input("Enter your age: ",value=None)

print(type(age))

#st.write("Your age is: ",age)

pressed= st.button("Enter to confirm",type="primary")

if pressed:
    st.write(f"Your name is {name} and your age is {age}")



#st.divider()

# PAssword

# password= st.text_input("Enter Your password",type="password")

# print(type(password))

# st.write("Your password is: ", password)