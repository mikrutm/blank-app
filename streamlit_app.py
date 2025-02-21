import streamlit as st
import pandas as pd

# Wczytanie pliku CSV
uploaded_file = st.file_uploader("Wybierz plik CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep=';', index_col=0) 
        
        st.dataframe(df, use_container_width=True, height=600)
    except Exception as e:
        st.error(f"Błąd podczas wczytywania pliku: {e}")
else:
    st.write("Załaduj plik CSV, aby zobaczyć dane.")
