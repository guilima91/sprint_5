import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv("vehicles.csv")
st.header("Análise de anúncios de veículos")

hist_button = st.button("Criar histograma")
if hist_button:
    st.write("Histograma de quilometragem")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

scatter_checkbox = st.checkbox("Mostrar dispersão")
if scatter_checkbox:
    st.write("Gráfico de dispersão: quilometragem X preço")
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter)
