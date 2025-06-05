import streamlit as st

st.title("Hello Everyone!")
st.write("This is a simple Streamlit app to demonstrate the use of the `st.title` function.")
user_input = st.text_input('Enter a custom message:', 'Hello, Hello Streamlit!')
st.write('Customized Message:', user_input)


