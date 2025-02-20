import streamlit as st
import pandas as pd

# Wczytanie pliku CSV
uploaded_file = st.file_uploader("Wybierz plik CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Wyświetlenie DataFrame w Streamlit z możliwością sortowania
    st.title("Wyświetlanie DataFrame w Streamlit")
    st.write("Przykładowa tabela danych:")
    st.dataframe(df, use_container_width=True)
else:
    st.write("Załaduj plik CSV, aby zobaczyć dane.")
