import streamlit as st
import pandas as pd
import plotly_express as px

data= pd.read_csv(r"C:\Users\marco\Documents\VS_TripTen_Work\VS_Code\TripletenSprint5\vehicles_us.csv")

st.header('Proyecto Sprint 5')

create_hist= st.checkbox('Histograma')

if create_hist:
    st.write('Se crea un histograma del conjunto de datos')

    hist= px.histogram(data, x='odometer')

    st.plotly_chart(hist, use_containter_width=True)

create_disp= st.checkbox('Gráfico de dispersión')

if create_disp:
    st.write('Se crea un gráfico de dispersión del conjunto de datos')

    disp= px.scatter(data, x='odometer', y='price')

    st.plotly_chart(disp,use_container_width=True)