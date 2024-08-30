import streamlit as st

st.header("Ask a question to the support team at vektir.ai :wave:")
st.write(f"Please fill out the form below and we will get back to you as soon as possible.")

with st.form(key='ask_question_form'):
    email = st.email_input(label='Email')
    question = st.text_area(label='Question')
    submit_button = st.form_submit_button(label='Submit')
    
    if submit_button:
        st.write(f"Thank you for your question. We will get back to you as soon as possible.")