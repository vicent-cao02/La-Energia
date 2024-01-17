from plotly import graph_objects as go


def crear_grafica_lineas(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Fecha'], y=df['MW disponibles'], mode='lines', name='MW disponibles'))
    fig.add_trace(go.Scatter(x=df['Fecha'], y=df['Demanda del dia'], mode='lines', name='Demanda del día'))
    fig.update_layout(title='Demanda del Día y MW Disponibles a lo Largo del Tiempo',
                      xaxis_title='Fecha',
                      yaxis_title='Megavatios (MW)')
    return fig


def crear_grafica_barras(df):                
    fig_b = go.Figure()
    fig_b.add_trace(go.Bar(x=df[thermoelectric], y=df[f_s], name='Fuera de servicio', marker_color='blue'))
    fig_b.add_trace(go.Bar(x=df[thermoelectric], y=df[m], name='En mantenimiento', marker_color='red'))
    fig_b.update_layout(
    title='Frecuencias de las termoeléctricas por estado',
    xaxis_title='Nombres de las termoeléctricas',
    yaxis_title='Frecuencia'
    )
    fig_b.update_layout(barmode='group')
