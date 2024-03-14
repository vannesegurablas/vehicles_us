import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Creación de gráficas para los vehiculos en US')      

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Quieres construir un histograma')
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.histogram(car_data, x="odometer")
        
    st.plotly_chart(fig, use_container_width=True)