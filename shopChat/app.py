import streamlit as st
import pandas as pd

from chat import anthropic_response, parse_response

# Title of the app
st.title('ShopChat')

# Sidebar for file uploader



# User input
user_input = st.text_input("What are you looking for?")

# Processing user input (just echoing it back in this example)
if user_input:
    response = anthropic_response(
        'fake_clothing_store_dataset.csv',
        user_input
    )
    parsed_response = parse_response(response[0].text)

    # Display recommendations
    st.header("Recommendations")
    for idx, recommendation in enumerate(parsed_response["recommendations"], start=1):
        st.info(f"{idx}. {recommendation}")

    # Display summary
    st.header("Summary")
    st.success(parsed_response["summary"])