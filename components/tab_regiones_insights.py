import streamlit as st
from utils import data_processor as dp
from components import charts as ch

def render_tab_regiones_insights(df):
    st.subheader("Rendimiento Regional")
    
    #  Indicador Global 
    todas_las_ciudades = dp.obtener_cuiddes(df)
    rendimiento_global = dp.rendimiento_mejorado_por_ciudades(df, todas_las_ciudades)
    
    if not rendimiento_global.empty:
        mejor_ciudad = rendimiento_global.iloc[0] 
        peor_ciudad = rendimiento_global.iloc[-1] 
        
        col1, col2 = st.columns(2)
        col1.success(f"Mayor porcentaje de mejora: **{mejor_ciudad['City']}** ({mejor_ciudad['Improved']:.1f}%)")
        col2.error(f" Menor porcentaje de mejora: **{peor_ciudad['City']}** ({peor_ciudad['Improved']:.1f}%)")

    # Selector multiple
    st.markdown("#### Comparativa Específica")
    ciudades_seleccionadas = st.multiselect(
        "Selecciona las ciudades a comparar:",
        options=todas_las_ciudades,
        default=[mejor_ciudad["City"],peor_ciudad['City']] #Valores por defeco
    )
    
    if ciudades_seleccionadas:
        df_rendimiento = dp.rendimiento_mejorado_por_ciudades(df, ciudades_seleccionadas)
        ch.grafico_comparativa_ciudades(df_rendimiento)
    else:
        st.warning("Selecciona al menos una ciudad para visualizar la comparativa.")

    # ---- COMUNICACIÓN DE DESCUBRIMIENTOS ----
    st.markdown("---")
    st.header(" Descubrimientos Clave (Insights)")
    st.markdown("Al explorar los datos de esta aplicación, surgen tres patrones fundamentales sobre cómo la IA moldea la educación:")

    with st.expander("1. Efectividad por Propósito: Coding vs. Writing"):
        st.write("El uso de herramientas de IA para **Coding** tiene una tasa de impacto positivo significativamente mayor en las calificaciones que su uso para **Writing**. Esto sugiere que la IA es altamente efectiva como asistente de lógica algorítmica y resolución de errores, pero puede ser contraproducente cuando los estudiantes la usan para que les redacte trabajos completos, afectando su desarrollo de habilidades.")

    with st.expander("2. La paradoja de Grammarly y el aprendizaje ilusorio"):
        st.write("Un hallazgo inesperado es que **Grammarly** registra el mayor porcentaje de notas en declive, y además, un grupo considerable afirma usarla como herramienta de **Learning** (Aprendizaje). Esto indica que depender en exceso de la autocorrección sin entender el porqué de los errores gramaticales genera una falsa sensación de conocimiento que se castiga en las evaluaciones reales.")

    with st.expander("3. Brecha de aprovechamiento geográfico"):
        st.write("Existe una adopción asimétrica de la tecnología. Mientras que los estudiantes en **Multan** están logrando capitalizar el uso de la IA para impulsar sus notas a un ritmo acelerado, los de **Karachi** muestran el índice más bajo de mejora. Esto subraya la necesidad de capacitar a los estudiantes no solo en *qué* herramientas usar, sino en *cómo* integrarlas de manera ética y efectiva según su contexto educativo.")