import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Creación de gráficas para los vehiculos en US')      

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Quieres construir un histograma según el modelo de los coches?')
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos segun el modelo de los coches')
            
    fig = px.histogram(car_data, x="model_year")
        
    st.plotly_chart(fig, use_container_width=True)


build_dispersion= st.checkbox('Quieres construir un diagrama de dispersión según el odométro?')
disp_button = st.button('Construir diagrama de dispersión') # crear un botón

if disp_button: # al hacer clic en el botón
    st.write('Creación de un diagrama de dispersión según el odométro de los coches vs su precio')
            
    fig = px.scatter(car_data, x="odometer", y="price")
        
    st.plotly_chart(fig, use_container_width=True)

build_pie= st.checkbox('Quieres saber las condiciones del coche según el modelo mediante un gráfico circular?')
pie_button = st.button('Construir gráfico circular')

if pie_button: # al hacer clic en el botón
    st.write('Creación de un gráfico circular según las condicones los coches')
            
    fig = px.pie(car_data, values='model_year', names='condition')
        
    st.plotly_chart(fig, use_container_width=True)

build_sun= st.checkbox('Quieres saber las condiciones del coche según el modelo mediante un gráfico sunburst?')
sun_button = st.button('Construir gráfico sunburst')

if sun_button: # al hacer clic en el botón
    st.write('Creación de un gráfico sunburst según las condiciones los coches')
    car_data = car_data.dropna(subset=['model_year'])
    fig = px.sunburst(
        car_data,
        path=["condition",'model_year'],
        values='cylinders',
    )
    st.plotly_chart(fig, use_container_width=True)