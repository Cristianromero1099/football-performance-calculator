import streamlit as st

# ======================================================
# CONFIGURACIÓN
# ======================================================

st.set_page_config(
    page_title="Football Performance Calculator",
    page_icon="⚽",
    layout="wide"
)

# ======================================================
# MENÚ LATERAL
# ======================================================

st.sidebar.title("⚽ Football Analytics")

pagina = st.sidebar.selectbox(
    "Selecciona un módulo",
    [
        "🏠 Inicio",
        "📊 Calculadora PPDA",
        "⚽ Calculadora xG",
        "🏃 Carga GPS",
        "📈 Dashboard"
    ]
)

# ======================================================
# INICIO
# ======================================================

if pagina == "🏠 Inicio":

    st.title("⚽ Football Performance Calculator")

    st.subheader("Plataforma de análisis táctico y rendimiento")

    st.write("""
Bienvenido.

Esta aplicación está pensada para analistas de rendimiento, videoanalistas
y analistas tácticos.

En las siguientes versiones incorporaremos:

• PPDA

• xG

• Dashboard

• GPS

• Big Data

• Machine Learning

• Lectura de archivos CSV

• Gráficos profesionales
""")

# ======================================================
# PPDA
# ======================================================

elif pagina == "📊 Calculadora PPDA":

    st.title("📊 Calculadora PPDA")

    st.markdown("### Introduce la información del partido")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        pases = st.number_input(
            "Pases del rival en campo propio",
            min_value=0,
            value=350
        )

        entradas = st.number_input(
            "Entradas",
            min_value=0,
            value=12
        )

        intercepciones = st.number_input(
            "Intercepciones",
            min_value=0,
            value=10
        )

        faltas = st.number_input(
            "Faltas",
            min_value=0,
            value=6
        )

    with col2:

        recuperaciones = st.number_input(
            "Recuperaciones",
            min_value=0,
            value=15
        )

        presiones = st.number_input(
            "Presiones",
            min_value=0,
            value=40
        )

        duelos = st.number_input(
            "Duelos defensivos ganados",
            min_value=0,
            value=18
        )

        despejes = st.number_input(
            "Despejes",
            min_value=0,
            value=9
        )

    st.divider()

    if st.button("📊 Calcular PPDA"):

        acciones = (
            entradas
            + intercepciones
            + faltas
            + recuperaciones
        )

        if acciones == 0:

            st.error("Las acciones defensivas deben ser mayores que cero.")

        else:

            ppda = pases / acciones

            st.header("Resultados")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "PPDA",
                round(ppda,2)
            )

            c2.metric(
                "Pases Rival",
                pases
            )

            c3.metric(
                "Acciones Defensivas",
                acciones
            )

            st.divider()

            if ppda <= 6:

                st.success("🔴 Presión Muy Alta")

            elif ppda <= 8:

                st.success("🟢 Presión Alta")

            elif ppda <= 10:

                st.info("🔵 Presión Media Alta")

            elif ppda <= 12:

                st.warning("🟡 Presión Media")

            elif ppda <= 15:

                st.warning("🟠 Presión Baja")

            else:

                st.error("⚫ Bloque Muy Bajo")

            st.progress(min(ppda/20,1.0))

            st.write("Interpretación:")

            st.write("""
- 0 - 6 → Presión Muy Alta

- 6 - 8 → Presión Alta

- 8 - 10 → Presión Media Alta

- 10 - 12 → Presión Media

- 12 - 15 → Presión Baja

- >15 → Bloque Muy Bajo
""")

# ======================================================
# XG
# ======================================================

elif pagina == "⚽ Calculadora xG":

    st.title("⚽ Calculadora xG")

    distancia = st.slider(
        "Distancia al arco (metros)",
        1,
        40,
        16
    )

    angulo = st.slider(
        "Ángulo de disparo",
        1,
        90,
        30
    )

    if st.button("Calcular xG"):

        xg = max(0.01, (1/distancia)*(angulo/90))

        st.metric(
            "xG Estimado",
            round(xg,2)
        )

# ======================================================
# GPS
# ======================================================

elif pagina == "🏃 Carga GPS":

    st.title("🏃 Carga GPS")

    distancia = st.number_input(
        "Distancia Total (m)",
        value=10500
    )

    hsr = st.number_input(
        "High Speed Running (m)",
        value=900
    )

    sprint = st.number_input(
        "Sprint Distance (m)",
        value=250
    )

    aceleraciones = st.number_input(
        "Aceleraciones",
        value=35
    )

    if st.button("Calcular Carga"):

        carga = (
            distancia*0.001
            + hsr*0.01
            + sprint*0.03
            + aceleraciones*0.5
        )

        st.metric(
            "Índice de Carga",
            round(carga,1)
        )

# ======================================================
# DASHBOARD
# ======================================================

elif pagina == "📈 Dashboard":

    st.title("📈 Dashboard del Partido")

    col1, col2, col3 = st.columns(3)

    col1.metric("PPDA","8.4")
    col2.metric("Posesión","58%")
    col3.metric("xG","1.85")

    col4, col5, col6 = st.columns(3)

    col4.metric("Tiros","15")
    col5.metric("Recuperaciones","57")
    col6.metric("Pases","542")

    st.info("En futuras versiones estos datos se cargarán automáticamente desde un archivo CSV.")
