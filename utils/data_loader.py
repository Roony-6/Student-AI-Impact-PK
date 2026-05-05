import pandas as pd
import streamlit as st

@st.cache_data
def load_data(filepath):
    """
    Carga el dataset y lo guarda en caché para optimizar el rendimiento.
    """
    df = pd.read_csv(filepath)
    return df