import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and introductory text
st.title("My first Streamlit app")
st.write("Hello Aryan")
st.text("Let's Start")

# Random data for charts
df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(df)
st.bar_chart(df)

# Sidebar
st.sidebar.title("Navigation")

# Media
st.image("https://4kwallpapers.com/images/walls/thumbs/17629.jpg", width=700)
st.video("https://www.youtube.com/watch?v=RVjE_YLBagc", width=900)

# CSV Upload
st.title("Upload Demon Slayer CSV")
uploaded_file = st.file_uploader("Choose your CSV file", type="csv")
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Here’s your CSV data:")
    st.dataframe(df_uploaded)

# User input
name = st.text_input("Enter name:")
if st.button("Welcome"):
    st.success(f"Hello, {name}")

# Header, subheader, markdown
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, `code`, [Link](https://streamlit.io)")
st.code("for i in range(5):\n    print(i)", language="python")

# Various interactive widgets (outside button)
st.text_input("What is your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose topping", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

# Matplotlib plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)
