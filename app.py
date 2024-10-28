import streamlit as st
import pandas as pd
import plotly.express as px

# Tema: Barra lateral de filtros

# Configuración de layout
st.set_page_config(layout="wide")

# Título del dashboard
st.title("Análisis Interactivo del Dataset Iris")

# Cargar el dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(url)

with st.sidebar:
    # Título de la barra lateral
    st.header("Filtros")

    # Selector de especie
    species = st.selectbox("Selecciona una especie de flor:", options=data["species"].unique())

    # Opciones para gráfico de dispersión
    x_axis = st.selectbox("Selecciona el eje X para el gráfico de dispersión:", options=data.columns[:4])
    y_axis = st.selectbox("Selecciona el eje Y para el gráfico de dispersión:", options=data.columns[:4])

    # Opciones para el histograma
    hist_column = st.selectbox("Selecciona la columna para el histograma:",
                               options=data.columns[:4], key="histogram")
    
    # Opciones para el gráfico de líneas
    line_x_axis = st.selectbox("Selecciona el eje X para el gráfico de líneas:", options=data.columns[:4],
                               index=0, key="line_x")
    line_y_axis = st.selectbox("Selecciona el eje Y para el gráfico de líneas:", options=data.columns[:4],
                               index=1, key="line_y")
    
filtered_data = data[data["species"] == species]

# Crear tres columnas para los gráficos
col1, col2, col3 = st.columns(3)

# Gráfico de dispersión para la primera columna
with col1:
    fig_scatter = px.scatter(filtered_data, x=x_axis, y=y_axis, color="species",
                             title=f"{x_axis} vs {y_axis} para {species}")
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    fig_hist = px.histogram(filtered_data, x=hist_column,
                            title=f"Distribución de {hist_column} para {species}")
    st.plotly_chart(fig_hist, use_container_width=True)

with col3:
    fig_line = px.line(filtered_data, x=line_x_axis, y=line_y_axis,
                       title=f"{line_x_axis} vs {line_y_axis} para {species}")
    st.plotly_chart(fig_line, use_container_width=True)