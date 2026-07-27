import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Football Performance Calculator",
    page_icon="⚽",
    layout="wide"
)

# Título principal
st.title("⚽ Football Performance Calculator")

st.markdown("### Herramienta para Análisis Táctico y Rendimiento")

st.divider()

st.write("""
Bienvenido.

Esta aplicación está diseñada para calcular indicadores de rendimiento
utilizados en el análisis táctico del fútbol.

En futuras versiones incluirá:

- 📊 Calculadora PPDA
- ⚽ Calculadora xG
- 🏃 Carga GPS
- 📈 Dashboard de KPIs
- 📂 Carga de archivos CSV
- 📉 Visualización de datos
""")
