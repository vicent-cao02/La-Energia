import streamlit as st
import pandas as pd
from data_processing import cargar_datos
from visualizations import crear_grafica_lineas
import os, folium, streamlit as st, pandas as pd, plotly.express as px, plotly.graph_objects as go
from datetime import datetime as dt
from streamlit_folium import folium_static

st.set_page_config(page_title="La Energía", page_icon=":bar_chart:")
st.title("La Energía")

# Cargar datos del JSON
db = cargar_datos('ddbb.json')

st.write("Este gráfico presenta la evolución de la demanda de energía eléctrica (línea azul oscura) comparada con la disponibilidad o capacidad de generación (línea azul clara) durante un período determinado.La línea azul oscura representa la demanda o carga del sistema eléctrico a lo largo del tiempo, medida en megavatios (MW). Esta demanda fluctúa a lo largo del día y los meses, dependiendo del consumo de los usuarios residenciales, comerciales e industriales.La línea azul clara muestra la capacidad disponible de generación eléctrica, es decir la máxima potencia que pueden entregar las centrales eléctricas al sistema, también en MW.Analizando ambas líneas podemos ver los períodos en que la demanda supera la disponibilidad, lo que puede ocasionar déficits o apagones en el servicio si no se toman acciones. También se observan los momentos en que hay capacidad ociosa por una baja demanda.Este tipo de gráfico es útil para que los operadores del sistema eléctrico analicen la evolución de la oferta y la demanda, y planifiquen acciones para garantizar el suministro de electricidad de forma eficiente y confiable.")
# Gráfica de Líneas con Plotly
fig = crear_grafica_lineas(db)
st.plotly_chart(fig)

st.write("El gráfico se le expone al usuario para que pueda observar la variación de estas dos variables durante el período de 2 años y pueda observar su comportamiento que es bastante inestable")

#Realizar los analisis
#un mapa con las localizaciones
st.subheader('Localización de las termoeléctricas')

#cargar el archivo de las localizaciones de las termoelectricas
df=pd.DataFrame(
    {
        
        "Latitude":[20.728433644751583,23.160837163922988,21.567053113289774,
                    23.019279319106403,23.1302452430394,23.10243454755323,
                    22.159797344832885,23.125633165882828,],
        'Longitude':[-75.5967566913524,-81.96305989167605,-77.2713085457038,
                        -82.74817643083628,-82.33771615913784,-81.52929387263102,
                        -80.45564991842924,-82.35890043084758],
        'Names':['CTE Lidio Ramón Pérez(Felton)','CTE Ernesto Guevara(Santa Cruz)','CTE Diez de Octubre(Nuevitas)','CTE Máximo Gómez(Mariel)',
                            'CTE Antonio Maceo(Renté)','CTE Antonio Guiteras','CTE Carlos M de Cespedes(Cienfuegos)',
                            "CTE Otto Parellada(Tallapiedra)"]
    }
)

mapa=folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=6)
for i in range(len(df)):
    folium.Marker([df.iloc[i]['Latitude'], df.iloc[i]['Longitude']], popup=df.iloc[i]['Names']).add_to(mapa)    
folium_static(mapa)
st.dataframe(df)
st.write("Este mapa muestra la ubicación de las principales termoeléctricas del país. Las termoeléctricas son centrales que generan energía eléctrica a partir de la combustión de recursos fósiles como gas natural, carbón o fuel oil. Analizando la distribución geográfica de las termoeléctricas podemos obtener valiosas perspectivas: Se observan concentraciones de centrales en ciertas zona Occidental. Esto constituye polos de generación eléctrica en el país. Gran parte de las termoeléctricas se localizan cerca de la costa, lo que facilita el enfriamiento de sus calderas de generacion. Las principales termoeléctricas se ubican relativamente cerca de las ciudades y zonas industrializadas de mayor demanda eléctrica. Esto reduce las pérdidas en transmisión. Existen amplias zonas del territorio sin cobertura de generación termoeléctrica, donde podría requerirse expansión de la capacidad instalada.Se identifican algunas termoeléctricas en zonas de alta biodiversidad o parques nacionales, lo que podría implicar impactos ambientales.Este tipo de análisis geoespacial es útil para la planificación estratégica, la toma de decisiones y la operación eficiente del sistema de suministro eléctrico.")