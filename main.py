import streamlit as st
import pandas

# Set the page layout to 'wide' for a two-column layout
st.set_page_config(layout="wide")

# Create two columns: col1 and col2
col1, col2 = st.columns(2)

# Column 1: Display an image
with col1:
    st.image("images/photo.png")

# Column 2: Display a title and informational content
with col2:
    st.title("Arifur Rahman")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    st.info(content)

st.write("My Apps")

# Create two columns: col3 and col4 for content layout
col3, col4 = st.columns(2)

# Read data from a CSV file using pandas
df = pandas.read_csv("data.csv", sep=";")

# Populate col3 with the first 10 rows of data
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

# Populate col4 with the remaining rows of data
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])