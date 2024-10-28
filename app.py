import streamlit as st
import pandas as pd
import plotly.express as px

# Tema: Otros tipos de gráficos

# Titulo
st.title("Análisis Interactivo del Dataset Iris")

# Cargando dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(url)

# Mostrar dataframe en Streamlit
st.write("Datos de ejemplo (iris dataset):")
st.write(data.head())

# Selector de especie
species = st.selectbox("Selecciona una especie de flor:", options=data["species"].unique())
filtered_data = data[data["species"] == species]

min_sepal_lenght, max_sepal_length = st.slider(
    "Selecciona el rango de Sepal Length:",
    min_value=float(data["sepal_length"].min()),
    max_value=float(data["sepal_length"].max()),
    value=(float(data["sepal_length"].min()), float(data["sepal_length"].max()))
)

filtered_data = filtered_data[(filtered_data["sepal_length"] >= min_sepal_lenght) &
                              (filtered_data["sepal_length"] <= max_sepal_length)]
st.write(f"Mostrando datos para Sepal Length en el rango de {min_sepal_lenght} a {max_sepal_length}")
st.write(filtered_data)

# Opciones para los ejes X e Y en el gráfico de dispersión
x_axis = st.selectbox("Selecciona el eje X para el gráfico de dispersión:", options=data.columns[:4])
y_axis = st.selectbox("Selecciona el eje Y para el gráfico de dispersión:", options=data.columns[:4])

# Gráfico de dispersión
fig_scatter = px.scatter(filtered_data, x=x_axis, y=y_axis, color="species",
                         title=f"{x_axis} vs {y_axis} para {species}")
st.plotly_chart(fig_scatter)

# Histograma
st.write("Histograma de la columna seleccionada")
hist_column = st.selectbox("Selecciona la columna para el histograma:", options=data.columns[:4])
fig_hist = px.histogram(filtered_data, x=hist_column, title=f"Distribución de {hist_column} para {species}")
st.plotly_chart(fig_hist)

# Gráfico de líneas
st.write("Gráfico de líneas entre características:")
line_x_axis = st.selectbox("Selecciona el eje X para el gráfico de líneas:",
                           options=data.columns[:4], index=0)
line_y_axis = st.selectbox("Selecciona el eje Y para el gráfico de líneas:",
                           options=data.columns[:4], index=1)
fig_line = px.line(filtered_data, x=line_x_axis, y=line_y_axis,
                   title=f"{line_x_axis} vs {line_y_axis} (Línea) para {species}")
st.plotly_chart(fig_line)