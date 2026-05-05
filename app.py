# app.py
import streamlit as st
from utils.data_loader import load_data
from utils import data_processor as dp
from components import charts as ch
from components import tab_impacto
# Configuración inicial
st.set_page_config(page_title="Student AI Impact PK", page_icon="🎓", layout="wide")
st.title("🎓 Impacto de la Inteligencia Artificial en Estudiantes PK")

# Cargar los datos
df = load_data('data/AI_Student_Life_Pakistan_2026.csv')

tab1, tab2, tab3 = st.tabs(["Impacto y Propósito", "Anomalías y Demografía", "Conclusiones (Insights)"])

with tab1:
    tab_impacto.render_tab_impacto(df)
