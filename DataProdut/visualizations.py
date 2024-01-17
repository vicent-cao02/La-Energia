from plotly import graph_objects as go 


def crear_grafica_lineas(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Fecha'], y=df['MW disponibles'], mode='lines', name='MW disponibles'))
    fig.add_trace(go.Scatter(x=df['Fecha'], y=df['Demanda del dia'], mode='lines', name='Demanda del día'))
    fig.update_layout(title='Demanda del Día y MW Disponibles a lo Largo del Tiempo',
                      xaxis_title='Fecha',
                      yaxis_title='Megavatios (MW)')
    return fig

