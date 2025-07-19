import pandas as pd

# Funciones reutilizables (limpieza de datos, carga, filtrado)
def limpiar_datos(df):
    df = df.dropna(subset=['Precio', 'Unidades vendidas'])
    df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')
    df['Unidades vendidas'] = pd.to_numeric(df['Unidades vendidas'], errors='coerce')
    df['Total_Venta'] = df['Precio'] * df['Unidades vendidas']
    return df
