# Student-AI-Impact-PK

```Student AI Impact Pakistan es un dashboard interactivo que analiza la adopción y el impacto de las herramientas de IA  en el rendimiento académico y la vida diaria de estudiantes en Pakistán durante el 2026.```
---

## Objetivos del Análisis
- Identificar qué herramientas de IA tienen mayor correlación con la mejora de notas.
- Comparar el impacto de la IA en tareas específicas como **Coding** vs. **Writing**.
- Analizar las disparidades de uso y resultados entre diferentes ciudades y niveles educativos.
- Detectar anomalías, como estudiantes con alta satisfacción pero rendimiento académico en declive.

## Estructura del proyecto
```text
├── app.py                  # Interfaz principal
├── components              # Componentes visuales
│   ├── charts.py           # Renderizacion de graficos
│   ├── __init__.py         
│   ├── tab_anomalias.py    # Vista anomalias
│   ├── tab_impacto.py      # Vista impacto
│   └── tab_regiones_insights.py    # Vista regiones e insights
├── data                    # Data
│   └── AI_Student_Life_Pakistan_2026.csv # Dataset
├── notebooks               
│   └── eda_ai_impact_pk.ipynb # Eda
├── README.md               # Documentacion proyecto (este archivo)
├── requirements.txt        # Dependencias
└── utils                   # Utilidades
    ├── data_loader.py      # Carga de datos
    ├── data_processor.py   # Procesador de datos
    └── __init__.py 
```

## Instalacion y uso (en local)
1. Clona el repositorio

```bash
git clone [git@github.com:Roony-6/Student-AI-Impact-PK.git](git@github.com:Roony-6/Student-AI-Impact-PK.git)

cd student-ai-impact-pk
```
2. Crea el entorno virtual

```bash
python -m venv venv
source venv/bin/activate
```
3. Instala las dependencias

```bash
pip install -r requirements.txt
```

4. Ejecuta el dashboard
```bash
streamlit run app.py
```

## 💡 Insights Clave Encontrados
- **Líder en Mejora:** ChatGPT muestra el mayor índice de impacto positivo en calificaciones (65%).
- **Uso por Ciudad:** Multan destaca como la ciudad con mayor aprovechamiento de estas herramientas.
- **Paradoja de Satisfacción:** Se identificó un segmento de usuarios que, a pesar de estar satisfechos, presentan un ligero declive en sus notas (principalmente usuarios de herramientas de gramática).

---