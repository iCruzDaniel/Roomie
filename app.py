import streamlit as st
import pandas as pd
from business_logic import inquilinos_compatibles
from aux_information import (
    generar_grafico_compatibilidad,
    generar_tabla_compatibilidad,
    obtener_id_inquilinos,
)

# Configuración inicial
st.set_page_config(layout="wide", page_title="Roomie", page_icon="./Media/logo.ico")
st.image('./Media/portada.png', use_container_width=True, caption="Encuentra a tus compañeros ideales")

# Encabezado principal
st.markdown(
    """
    <style>
        .main-header {
            text-align: center;
            font-size: 2.5em;
            color: #ED3163;
            font-weight: bold;
            margin-top: 30px;
        }
        .divider {
            border: 1px solid #ED3163;
            margin: 20px 0;
        }
    </style>
    <div class="main-header">Encuentra a tus Compañeros de Piso Ideales</div>
    <div class="divider"></div>
    """,
    unsafe_allow_html=True
)

# Sidebar para entrada de datos
with st.sidebar:
    st.header("Configuración de Búsqueda")
    st.markdown(
        """
        <style>
            .sidebar-header {
                font-size: 1.2em;
                font-weight: bold;
                color: #34495E;
                margin-bottom: 10px;
            }
            .sidebar-input {
                border: 2px solid #ED3163;
                border-radius: 5px;
                padding: 5px;
                margin-bottom: 10px;
            }
            .sidebar-button {
                background-color: #ED3163;
                color: white;
                font-weight: bold;
                border: none;
                padding: 10px;
                border-radius: 5px;
                cursor: pointer;
            }
            .sidebar-button:hover {
                background-color: #D12D56;
            }
        </style>
        <div class="sidebar-header">¿Quién está viviendo ya en el piso?</div>
        """,
        unsafe_allow_html=True
    )
    inquilinos = [st.text_input(f"Inquilino {i+1} (Nombre o ID)", placeholder="Ejemplo: Juan Pérez") for i in range(3)]
    num_compañeros = st.text_input("¿Cuántos nuevos compañeros quieres buscar?", placeholder="Número de compañeros")

    st.markdown(
        "<div style='margin-top: 20px;'></div>", unsafe_allow_html=True
    )
    buscar = st.button("🔍 Buscar Compañeros", key="buscar", help="Presiona para iniciar la búsqueda")

# Procesamiento cuando se presiona el botón
if buscar:
    try:
        topn = int(num_compañeros)
        id_inquilinos = obtener_id_inquilinos(*inquilinos, topn)
        resultado = inquilinos_compatibles(id_inquilinos, topn) if id_inquilinos else None
    except ValueError:
        st.error("Por favor, ingresa un número válido para el número de compañeros.")
        resultado = None
else:
    resultado = None

# Mostrar resultados
if isinstance(resultado, str):  # Mensaje de error
    st.error(resultado)
elif resultado:  # Mostrar gráficos y tabla
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Resultados de Compatibilidad")
    
    col1, col2 = st.columns((1, 2))

    with col1:
        st.markdown(
            """
            <style>
                .result-header {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #ED3163;
                }
            </style>
            <div class="result-header">Nivel de compatibilidad:</div>
            """,
            unsafe_allow_html=True
        )
        st.pyplot(generar_grafico_compatibilidad(resultado[1]))

    with col2:
        st.markdown(
            """
            <style>
                .result-header {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #ED3163;
                }
            </style>
            <div class="result-header">Comparativa de compañeros:</div>
            """,
            unsafe_allow_html=True
        )
        st.plotly_chart(generar_tabla_compatibilidad(resultado), use_container_width=True)

# Pie de página
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #7F8C8D;
            margin-top: 50px;
        }
        .footer a {
            color: #ED3163;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="footer">Powered by Streamlit · <a href="#">Encuentra a tus compañeros perfectos</a></div>
    """,
    unsafe_allow_html=True
)
