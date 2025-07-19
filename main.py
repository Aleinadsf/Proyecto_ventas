import pandas as pd
from utils import cargar_datos, limpiar_datos
from analisis_numpy import calcular_estadisticas
from analisis_pandas import (
    mostrar_estadisticas_generales,
    filtrar_poco_vendidos,
    filtrar_por_fecha,
    ventas_por_categoria,
    filtrar_dulces_oct_dic,
    mostrar_ventas_por_categoria,
    convertir_a_lista_productos,
    contar_productos_por_categoria
)
# se crearon las funciones: para procesar los datos y otra para generar los resultados.
def procesar_datos(ventas):
    ventas = limpiar_datos(ventas)
    ventas["Fecha"] = pd.to_datetime(ventas["Fecha"])
    return ventas

def generar_resultados(ventas):
    ventas_np = ventas['Total_Venta'].to_numpy()
    estadisticas = calcular_estadisticas(ventas_np)
    lista_productos = convertir_a_lista_productos(ventas)

    print("\n-----------ANÁLISIS ESTADÍSTICOS DE LAS VENTAS---------------")
    for clave, valor in estadisticas.items():
        print(f"{clave.capitalize()}: {valor:.2f}")

    mostrar_estadisticas_generales(ventas)
    filtrar_poco_vendidos(ventas)
    filtrar_por_fecha(ventas, mes=8, anio=2025)
    filtrar_dulces_oct_dic(ventas)
    mostrar_ventas_por_categoria(ventas)
    ventas_por_categoria(ventas)

    print("\nProductos en lista:")
    for producto in lista_productos[:5]:
        print(f"{producto.nombre} - {producto.total_venta():.2f}")
    
    return lista_productos

if __name__ == "__main__":
    ventas = cargar_datos('PF_GRUPO.csv')
    ventas = procesar_datos(ventas)
    lista_productos = generar_resultados(ventas)
    contar_productos_por_categoria(lista_productos)
