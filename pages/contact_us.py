import streamlit as st
from send_email import send_email

# Display a header for the contact form
st.header("Contact Me")

# Create a form using Streamlit with email input and message textarea
with st.form(key="email_form"):
    user_email = st.text_input("Your Email")
    raw_message = st.text_area("Your Message")

    # Create an email message with a subject and content
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    # Add a form submission button
    button = st.form_submit_button("Send")
    if button:
        send_email(message)
        st.info("Your email has been sent successfully!")