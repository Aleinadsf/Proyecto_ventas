import pandas as pd
from utils import limpiar_datos
from analisis_numpy import calcular_estadisticas
from analisis_pandas import (
    mostrar_estadisticas_generales,
    filtrar_poco_vendidos,
    filtrar_por_fecha,
    ventas_por_categoria,
    filtrar_dulces_oct_dic,
    mostrar_ventas_por_categoria
)


ventas = pd.read_csv('PF_GRUPO.csv')
ventas = limpiar_datos(ventas)
ventas["Fecha"] = pd.to_datetime(ventas["Fecha"])

ventas_np = ventas['Total_Venta'].to_numpy()
estadisticas = calcular_estadisticas(ventas_np)

# Análisis con NumPy
print("\n-----------ANÁLISIS ESTADÍSTICOS DE LAS VENTAS---------------")
for clave, valor in estadisticas.items():
    print(f"{clave.capitalize()}: {valor:.2f}")

# Análisis con Pandas
mostrar_estadisticas_generales(ventas)
filtrar_poco_vendidos(ventas)
filtrar_por_fecha(ventas, mes=8, anio=2025)
filtrar_dulces_oct_dic(ventas)
mostrar_ventas_por_categoria(ventas)
ventas_por_categoria(ventas)