"""Sprint 6 Project"""
import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')

hist_create = st.button('Make histogram')
scatter_create = st.button('Make scatter chart')

if hist_create:
    st.write('Make histogram for vehicles data')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if scatter_create:
    st.write('Make scatter chart for vehicles data')

    fig = px.scatter(car_data, x="odometer", y='price')

    st.plotly_chart(fig)
# End of line
# EOF