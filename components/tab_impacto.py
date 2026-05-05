import streamlit as st
from utils import data_processor as dp
from components import charts as ch

def render_tab_impacto(df):
    st.subheader("Análisis de Impacto por Herramienta")
    
    # Obtenr las todas las ciudades 
    ciudad_seleccionada = st.selectbox(
        "Selecciona una región",
        ["Todas las ciudades"] + dp.obtener_cuiddes(df)
    )
    
    # Obtener KPIs genrales
    kpis = dp.obtener_KPI_ciudad(df, ciudad_seleccionada)
    
    #df impacto cada herramienta por ciudad seleccionada
    df_impacto_herramienta_por_ciudad = dp.impacto_por_ciudad(df, ciudad=ciudad_seleccionada)
    
    #df impacto cada herramientas todas las ciudades
    df_impacto_por_herramienta = dp.proporcion_impacto_por_herramientaIA(df)
    
    # mostrar kpis 
    st.markdown("#### Resumen Rápido")
    col1, col2, col3 = st.columns(3)
    col1.metric("Estudiantes Encuestados", str(kpis.get("total_encuestados"))) 
    col2.metric("Herramienta Dominante", str(kpis.get("herramienta_dominante")))
    col3.metric("Impacto Positivo General", str(kpis.get("impacto_positivo_general")))
    
    st.markdown("---")
    
   
    col1, col2 = st.columns([1,2])
    with col1:
        if ciudad_seleccionada == "Todas las ciudades":
            st.dataframe(df_impacto_por_herramienta)
        else:
            st.dataframe(df_impacto_herramienta_por_ciudad)
            
    with col2:
        if ciudad_seleccionada == "Todas las ciudades":
            ch.grafico_barras(df_impacto_por_herramienta)
        else:
            ch.grafico_barras(df_impacto_herramienta_por_ciudad)
            
        
    with st.expander(f"Ver registros de {ciudad_seleccionada}"):
        st.write("Explora los datos utilizados para generar este análisis:")
        st.dataframe(df_impacto_herramienta_por_ciudad)
        
    # --- COMPARATIVAS IMPACto POR PROPOSItO ---
    st.markdown("---")
    st.subheader("Comparativa de Propósitos: Uso de la IA")
    

##comentario: Faltaria agregarlo por ciudad????
    lista_propositos = dp.obtener_propositos(df)
    proposito_seleccionado = st.radio("Selecciona para qué usan la IA:", lista_propositos, horizontal=True)
    datos_proposito = dp.impacto_por_proposito(df, proposito_seleccionado)
    ch.grafico_impacto_proposito(datos_proposito)