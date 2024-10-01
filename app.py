"""Sprint 6 Project"""
import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Cart Data Chart With Checkboxes')
car_data = pd.read_csv('vehicles_us.csv')

hist_create = st.checkbox('Make histogram')
scatter_create = st.checkbox('Scatter Chart')

if hist_create:
    st.write('Make histogram for vehicles data')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True) #crear el grafico de histograma

if scatter_create:
    st.write('Make scatter chart')
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.show()  # crear gráfico de dispersión

# End of line
