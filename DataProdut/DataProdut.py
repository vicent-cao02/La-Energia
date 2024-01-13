import os, folium, streamlit as st, pandas as pd
from streamlit_folium import folium_static
import plotly.express as px
import matplotlib.pyplot as plt
import json
from collections import Counter

st.set_page_config(page_title="LA Energía",\
                   page_icon=":bar_chart:",
                   )


db=pd.read_json(os.path.join(os.path.dirname(__file__), '..', 'base de datos.json'))
db=db.transpose() # Transponer el dataframe
db = db.drop('Info', axis=1)

with st.container():
    st.title("La Energía")

   import streamlit as st
import json
from collections import Counter
import matplotlib.pyplot as plt

# Cargar los datos del JSON
@st.cache
def cargar_datos(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Generar gráfica circular
def generar_grafica_circular(data, title, key):
    conteo = Counter(data[key])
    plt.figure(figsize=(8, 8))
    plt.pie(conteo.values(), labels=conteo.keys(), autopct='%1.1f%%', startangle=140)
    plt.title(title)
    return plt

# Streamlit App
def main():
    st.title("Análisis de Termoeléctricas")

    # Cargar datos
    datos = cargar_datos("ruta/a/tu/archivo.json")

    # Gráfica Circular - Fuera de Servicio
    st.header("Termoeléctricas Fuera de Servicio")
    fig1 = generar_grafica_circular(datos, 'Termoeléctricas Fuera de Servicio', 'Termoelectricas fuera de servicio')
    st.pyplot(fig1)

    # Gráfica Circular - En Mantenimiento
    st.header("Termoeléctricas en Mantenimiento")
    fig2 = generar_grafica_circular(datos, 'Termoeléctricas en Mantenimiento', 'Termoelectricas en mantenimiento')
    st.pyplot(fig2)

if __name__ == "__main__":
    main()
import streamlit as st
import json
import matplotlib.pyplot as plt

# Cargar los datos del JSON
@st.cache
def cargar_datos(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Generar gráfica de barras
def generar_grafica_barras(data):
    categorias = ['MW indisponibles por averías', 'MW en mantenimiento', 'MW limitados en la generación térmica']
    valores = [data['MW indisponibles por averias'], data['MW en mantenimiento'], data['MW limitados en la generacion termica']]
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, valores, color=['blue', 'green', 'red'])
    plt.title('Indisponibilidad de MW por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('MW')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

# Streamlit App
def main():
    st.title("Análisis de Indisponibilidad de MW")

    # Cargar datos
    datos = cargar_datos("ruta/a/tu/archivo.json")

    # Gráfica de Barras
    st.header("Indisponibilidad de MW por Categoría")
    fig = generar_grafica_barras(datos)
    st.pyplot(fig)

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Streamlit App para Gráfica de Líneas (Demanda del día y MW disponibles)
def main():
    st.title("Gráfica de Líneas - Demanda del día y MW disponibles")

    # Crear datos hipotéticos para la gráfica
    fechas = pd.date_range(start='2023-01-01', periods=30, freq='D')
    demanda_dia = np.random.randint(1000, 2000, size=30)  # Valores aleatorios entre 1000 y 2000
    mw_disponibles = np.random.randint(1500, 2500, size=30)  # Valores aleatorios entre 1500 y 2500

    # Crear un DataFrame
    df = pd.DataFrame({
        'Fecha': fechas,
        'Demanda del día': demanda_dia,
        'MW disponibles': mw_disponibles
    })

    # Gráfica de líneas
    plt.figure(figsize=(10, 6))
    plt.plot(df['Fecha'], df['Demanda del día'], label='Demanda del día')
    plt.plot(df['Fecha'], df['MW disponibles'], label='MW disponibles')
    plt.xlabel('Fecha')
    plt.ylabel('MW')
    plt.title('Demanda del día vs MW disponibles')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Mostrar la gráfica
    st.pyplot(plt)

if __name__ == "__main__":
    main()

import streamlit as st
import json
from collections import Counter
import matplotlib.pyplot as plt

# Cargar los datos del JSON
@st.cache
def cargar_datos(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Generar gráfica de barras
def generar_grafica_barras(data, title, key):
    conteo = Counter(data[key])
    plt.figure(figsize=(10, 6))
    plt.bar(conteo.keys(), conteo.values())
    plt.title(title)
    plt.xlabel('Termoeléctricas')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

# Streamlit App
def main():
    st.title("Análisis de Datos de Termoeléctricas")

    # Cargar datos
    datos = cargar_datos("ruta/a/tu/archivo.json")

    # Gráficas
    st.header("Termoeléctricas Fuera de Servicio")
    fig1 = generar_grafica_barras(datos, 'Termoeléctricas Fuera de Servicio', 'Termoelectricas fuera de servicio')
    st.pyplot(fig1)

    st.header("Termoeléctricas en Mantenimiento")
    fig2 = generar_grafica_barras(datos, 'Termoeléctricas en Mantenimiento', 'Termoelectricas en mantenimiento')
    st.pyplot(fig2)

if __name__ == "__main__":
    main()

import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos del JSON
@st.cache
def cargar_datos(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Generar datos simulados para el gráfico de área
def generar_datos_simulados(data):
    # Suponiendo que 'Máxima afectación' varía cada día durante un mes
    fechas = pd.date_range(start='2023-01-01', end='2023-01-31')
    max_afectacion = np.random.choice(range(0, data['Maxima afectacion'] + 1), len(fechas))
    df = pd.DataFrame({'Fecha': fechas, 'Maxima afectacion': max_afectacion})
    return df

# Generar gráfico de área
def generar_grafico_area(df):
    plt.figure(figsize=(10, 6))
    plt.fill_between(df['Fecha'], df['Maxima afectacion'], color="skyblue", alpha=0.4)
    plt.plot(df['Fecha'], df['Maxima afectacion'], color="Slateblue", alpha=0.6)
    plt.title('Máxima Afectación a lo Largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Máxima Afectación')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

# Streamlit App
def main():
    st.title("Análisis de Máxima Afectación")

    # Cargar datos
    datos = cargar_datos("\datos_saneados.json")

    # Generar datos simulados
    datos_simulados = generar_datos_simulados(datos)

    # Gráfico de Área
    st.header("Máxima Afectación a lo Largo del Tiempo")
    fig = generar_grafico_area(datos_simulados)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
