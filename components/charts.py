import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from utils import data_processor as dp

def grafico_barras(df:pd.DataFrame):
    """
    Recibe un DataFrame con porcentajes y renderiza un grafico.
    """
    st.bar_chart(df, x_label="AI tool", y_label="Percent")

def grafico_impacto_proposito(serie_impacto):
    """Renderiza un gráfico de barras para el impacto según el propósito."""
    st.bar_chart(serie_impacto)