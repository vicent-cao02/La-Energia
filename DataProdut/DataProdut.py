import os, folium, streamlit as st, pandas as pd
from streamlit_folium import folium_static
import plotly.express as plt
import matplotlib.pyplot as plt
import json
from collections import Counter
import plotly.graph_objects as go

st.set_page_config(page_title="La Energía",\
                   page_icon=":bar_chart:",
                   )
st.title("La Energía")

db = pd.read_json(os.path.join(os.path.dirname(__file__), '..', 'base de datos.json')).transpose().reset_index()
db.rename(columns={'index': 'Día'}, inplace=True)
db['Día'] = db['Día'].astype(str).str.split().str[0]
st.write(db)

#db=pd.read_json(os.path.join(os.path.dirname(__file__), '..', 'base de datos.json'))
#db=db.transpose() # Transponer el dataframe
#db = db.drop('Info', axis=1)

#print(db.columns)

fig = go.Figure()
fig.add_trace(go.Scatter(x = db["Día"], y = db['MW disponibles'], name = 'MW disponibles'))
fig.add_trace(go.Scatter(x = db["Día"], y = db['Demanda del dia'], name = 'Demanda del dia'))
st.plotly_chart(fig)


st.subheader('Frecuencias de las termoeléctricas por estado')
# Crear un selectbox para seleccionar el año
year = st.selectbox("Seleccione un año", db['Año'].unique())
# Filtrar el dataframe basado en la selección del usuario
filtrado = db[db['Año'] == year]
    
thermoelectric=[]
for i in filtrado['Termoelectricas en mantenimiento']:
    if i:
        for j in i:
            if j not in thermoelectric:
                thermoelectric.append(j)
for i in filtrado['Termoelectricas fuera de servicio']:
    if i:
        for j in i:
            if j not in thermoelectric:
                thermoelectric.append(j)

f_s=[]#almacena la cantidad de veces q se repiten las unidades q estan fuera de servicio 
for j in thermoelectric:
    c=0   
    for i in filtrado['Termoelectricas fuera de servicio']:
        if i :
            if j in i:
                c+=1
    f_s.append(c)

m=[]#se almacenan la cantidad de veces q se repiuten cuando estan en mantenimineto
for i in thermoelectric:
    c=0
    for j in filtrado['Termoelectricas en mantenimiento']:
        if j :
            if i in j:
                c+=1
    m.append(c)
                

fig_b = go.Figure()

fig_b.add_trace(go.Bar(x=thermoelectric, y=f_s, name='Fuera de servicio', marker_color='blue'))
fig_b.add_trace(go.Bar(x=thermoelectric, y=m, name='En mantenimiento', marker_color='red'))
fig_b.update_layout(
title='Frecuencias de las termoeléctricas por estado',
xaxis_title='Nombres de las termoeléctricas',
yaxis_title='Frecuencia'
)
fig_b.update_layout(barmode='group')

st.plotly_chart(fig_b)