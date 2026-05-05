import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from utils import data_processor as dp
import seaborn as sns
import plotly.express as px

def grafico_barras(df:pd.DataFrame):
    """
    Recibe un DataFrame con porcentajes y renderiza un grafico.
    """
    st.bar_chart(df, x_label="AI tool", y_label="Percent")

def grafico_impacto_proposito(serie_impacto):
    """Renderiza un gráfico de barras para el impacto según el propósito."""
    st.bar_chart(serie_impacto)
    
    
def grafico_demografia_horas(df, desglosar_genero, desglosar_educacion):
    """
    Renderiza un boxplot dinámico basado en las selecciones del usuario
    """
    if desglosar_educacion and desglosar_genero:
        fig = px.box(df,x="Education_Level",y="Daily_Usage_Hours",color="Gender",points="all",title="Distribución de Horas por Nivel Educativo y Género")
    elif desglosar_genero:
        fig = px.box(df,x="Gender",y="Daily_Usage_Hours",points="all",title="Distribución de Horas por Género")
    elif desglosar_educacion:
        fig = px.box(df,x="Education_Level",y="Daily_Usage_Hours",points="all",title="Distribución de Horas por Nivel Educativo")
    else:
        fig = px.box(
            df, 
            y="Daily_Usage_Hours", 
            points="all",
            title="Distribución General de Horas de Uso Diario"
        )
    st.plotly_chart(fig)
    
    
    
def grafico_comparativa_ciudades(df_rendimiento):
    """
    Renderiza un gráfico de barras comparando el porcentaje de mejora entre ciudades.
    """
    fig = px.bar(
        df_rendimiento,
        x='City',
        y='Improved',
        title="Porcentaje de Notas Mejoradas por Ciudad",
        color='City',
        text_auto='.1f' # Muestra el valor exacto sobre la barra con un decimal
    )
    
    fig.update_layout(
        yaxis_title="Porcentaje (%)", 
        xaxis_title="Ciudad", 
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)