import streamlit as st
import pandas as pd 
df = pd.read_csv("konsultacje.csv")
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.dataframe(df)