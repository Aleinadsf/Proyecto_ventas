import numpy as np
# import pandas as pd

# -----------se movio a main.py
# ventas = pd.read_csv('PF_GRUPO.csv')

# # limpieza de datos
# ventas = ventas.dropna(subset=['Precio','Unidades vendidas'])
# ventas['Precio'] = pd.to_numeric(ventas['Precio'], errors='coerce')
# ventas['Unidades vendidas'] = pd.to_numeric(ventas['Unidades vendidas'], errors='coerce')

# # calcular total por venta
# ventas['Total venta'] = ventas['Precio'] * ventas['Unidades vendidas']
# ventas_np = ventas['Total venta'].to_numpy()

# funcion para calcular estadisticas
def calcular_estadisticas(ventas_np):
    return{
        "promedio": np.mean(ventas_np),
        "desviacion_estandar": np.std(ventas_np),
        "mediana": np.median(ventas_np),
        "minimo": np.min(ventas_np),
        "maximo": np.max(ventas_np)
    }
# -----------se movio a main.py
# estadisticas = calcular_estadisticas(ventas_np)

# # mostar resultados
# print("\n-----------ANALISIS ESTADÍSTICOS DE LAS VENTAS---------------")
# for clave, valor in estadisticas.items():
#     print(f"{clave.capitalize()}: {valor:.2f}")
