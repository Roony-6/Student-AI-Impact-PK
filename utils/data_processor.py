import pandas as pd
import streamlit as st

# ----1 Proporcion del impacto segmentado por herramientas de IA----
@st.cache_data

def proporcion_impacto_por_herramientaIA(df: pd.DataFrame) -> pd.DataFrame:
    ''''''
    impacto_por_herramientaIA = df.groupby("AI_Tool_Used")["Impact_on_Grades"].value_counts(normalize=True).unstack() * 100
    return impacto_por_herramientaIA

@st.cache_data
def obtener_cuiddes(df: pd.DataFrame)-> list:
    ciudades = list(df["City"].unique())
    return ciudades

def impacto_por_ciudad(df,ciudad):
    df_ciudad_seleccionada = df[df['City'] == ciudad]
    impacto_por_ciudad = df_ciudad_seleccionada.groupby("AI_Tool_Used")["Impact_on_Grades"].value_counts(normalize=True).unstack() * 100
    return impacto_por_ciudad

def obtener_KPI_ciudad(df: pd.DataFrame,ciudad)->dict:
    """Obtiene los kpis principales y los devuelve en un diccionario"""
    total_encuestados = 0
    herramienta_dominante = ''
    impacto_positivo_general = ''
    kpis={}
    if ciudad == "Todas las ciudades":
        total_encuestados = len(df)
        herrameinta_dominante = df["AI_Tool_Used"].value_counts().idxmax()    
        impacto_positivo_general = proporcion_impacto_por_herramientaIA(df)["Improved"].mean()
        kpis ={"total_encuestados":total_encuestados,
               "herramienta_dominante":herrameinta_dominante,
               "impacto_positivo_general":impacto_positivo_general}
        return kpis
    else:
        df_ciudad = df[df['City'] == ciudad]
        total_encuestados = len(df_ciudad)
        herrameinta_dominante = df_ciudad["AI_Tool_Used"].value_counts().idxmax()    
        impacto_positivo_general = impacto_por_ciudad(df,ciudad=ciudad)["Improved"].mean()
        kpis ={"total_encuestados":total_encuestados,
               "herramienta_dominante":herrameinta_dominante,
               "impacto_positivo_general":impacto_positivo_general}
        return kpis
        


def obtener_propositos(df):
    """Devuelve una lista con los propósitos de uso únicos."""
    return df['Purpose'].unique().tolist()

def impacto_por_proposito(df, proposito):
    """Calcula el porcentaje de impacto en notas para un propósito específico."""
    df_filtrado = df[df['Purpose'] == proposito]
    # Calculamos la frecuencia relativa (porcentajes)
    impacto = df_filtrado['Impact_on_Grades'].value_counts(normalize=True) * 100
    return impacto

# ----- ANOMALIAS Y DEMOGRAFIA -----

def obtener_anomalias(df: pd.DataFrame, min_hours_usage, max_hours_usage):
    ''''Obtener df nivel de satisfaccion alto pero con notas en declive'''
    filtro_anomalias = ((df["Satisfaction_Level"] == "High") & (df["Impact_on_Grades"] == "Slight Decline")
                        & (df["Daily_Usage_Hours"] >= min_hours_usage) & (df["Daily_Usage_Hours"] <= max_hours_usage))
    return df[filtro_anomalias]

def obtener_distribucion_genero(df: pd.DataFrame):
    return df['Gender'].value_counts()

def obtener_distribucion_nivel_educativo(df: pd.DataFrame):
    return df['Education_Level'].value_counts()