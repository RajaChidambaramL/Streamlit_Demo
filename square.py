import streamlit as st

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")

if st.button("Submit"):
    st.write('The current number is ', number*number)
else:
    st.write('Please enter a value and click submit')