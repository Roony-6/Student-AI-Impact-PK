import streamlit as st
from utils import data_processor as dp  
from components import charts as ch

def render_tab_anomalias(df):
    st.subheader("Análisis de Anomalías: Satisfacción vs Rendimiento")
    st.markdown("Exploramos casos donde los estudiantes están muy satisfechos con la IA, pero sus notas han disminuido")
    
    min_horas_df = float(df['Daily_Usage_Hours'].min())
    max_horas_df = float(df['Daily_Usage_Hours'].max())
    
    rango_horas = st.slider(
        "Filtra por Horas de Uso Diario:",
        min_value=min_horas_df,
        max_value=max_horas_df,
        value=(min_horas_df, max_horas_df), # Selecciona todo el rango por defecto
        step=0.5
    )
    
    # Obtener los datos filtrados
    df_anomalias = dp.obtener_anomalias(df,rango_horas[0],rango_horas[1])
    
    # Mostar cantidad
    st.metric("Total de Estudiantes en esta condición", len(df_anomalias))
    
    #  mostrar df
    st.markdown("#### Detalle de estudiantes y herramientas usadas")
    if not df_anomalias.empty:
        # Mostramos solo las columnas relevantes
        columnas_mostrar = ['Student_ID', 'AI_Tool_Used', 'Daily_Usage_Hours', 'Purpose', 'City']
        st.dataframe(df_anomalias[columnas_mostrar], use_container_width=True)
    else:
        st.info("No hay estudiantes que cumplan con estos criterios en el rango de horas seleccionado.")
        
        
    # ---- DEMOGRAFIA -----
    st.markdown("---")
    st.subheader("Demografía y Patrones de Uso")
    st.markdown("Analiza cómo se distribuye el tiempo de uso diario de la IA según el perfil del estudiante.")

    
    # Mostramos cuantos hombres/mujeres o estudiantes por nivel hay en total
    col_metricas1, col_metricas2 = st.columns(2)
    with col_metricas1:
        st.caption("Distribución por Género en el dataset:")
        st.dataframe(dp.obtener_distribucion_genero(df=df_anomalias), use_container_width=True)
    with col_metricas2:
        st.caption("Distribución por Nivel Educativo:")
        st.dataframe(dp.obtener_distribucion_nivel_educativo(df=df_anomalias), use_container_width=True)

    st.markdown("#### Configuración de la Gráfica")
    
    col_check1, col_check2 = st.columns(2)
    with col_check1:
        desglosar_genero = st.checkbox("Desglosar por Género (Gender)", value=True)
    with col_check2:
        desglosar_educacion = st.checkbox("Desglosar por Nivel Educativo (Education_Level)", value=False)

    # grafico
    ch.grafico_demografia_horas(df, desglosar_genero, desglosar_educacion)