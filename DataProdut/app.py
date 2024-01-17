import streamlit as st
from data_processing import cargar_datos
from visualizations import crear_grafica_lineas, crear_grafica_barras

st.set_page_config(page_title="La Energía", page_icon=":bar_chart:")
st.title("La Energía")

# Cargar datos del JSON
db = cargar_datos('ddbb.json')

# Gráfica de Líneas con Plotly
fig = crear_grafica_lineas(db)
st.plotly_chart(fig)


thermoelectric=[]
for i in db['Termoelectricas en mantenimiento']:
    if i:
        for j in i:
            if j not in thermoelectric:
                thermoelectric.append(j)
for i in db['Termoelectricas fuera de servicio']:
    if i:
        for j in i:
            if j not in thermoelectric:
                thermoelectric.append(j)

f_s=[]#almacena la cantidad de veces q se repiten las unidades q estan fuera de servicio 
for j in thermoelectric:
    c=0   
    for i in db['Termoelectricas fuera de servicio']:
        if i :
            if j in i:
                c+=1
    f_s.append(c)

m=[]#se almacenan la cantidad de veces q se repiuten cuando estan en mantenimineto
for i in thermoelectric:
    c=0
    for j in db['Termoelectricas en mantenimiento']:
        if j :
            if i in j:
                c+=1
    m.append(c)
                
# Frecuencias de las termoeléctricas por estado
st.subheader('Frecuencias de las termoeléctricas por estado')
fig_b = crear_grafica_barras()
st.plotly_chart(fig_b)