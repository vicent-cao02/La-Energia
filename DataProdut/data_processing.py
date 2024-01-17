import pandas as pd
import json

def cargar_datos(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame.from_dict(data, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Fecha'}, inplace=True)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    return df
breakpoint()