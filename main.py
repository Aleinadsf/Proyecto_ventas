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
    contar_productos_por_categoria,
    graficar_ventas_por_categoria,
    graficar_ventas_por_fecha,
    graficar_dulces_oct_dic,
)
# se crearon las funciones: para procesar los datos y otra para generar los resultados.
def procesar_datos(ventas):
    ventas = limpiar_datos(ventas)
    ventas["Fecha"] = pd.to_datetime(ventas["Fecha"])
    return ventas
#Generacion de resultados: se calcula las estadisticas, se convierte a lista de productos y se muestran los resultados.
def generar_resultados(ventas):
    ventas_np = ventas['Total_Venta'].to_numpy()
    estadisticas = calcular_estadisticas(ventas_np)
    lista_productos = convertir_a_lista_productos(ventas)
# Se muestran los resultados de las estadisticas y los productos.
    print("\n" + "="*60)
    print("🔍 ANÁLISIS ESTADÍSTICOS DE LAS VENTAS".center(60))
    print("="*60)
    for clave, valor in estadisticas.items():
        print(f"{clave.capitalize():<20}: {valor:.2f}")
#Estadisticas generales con panda: se muestran las estadisticas generales, los productos con ventas menores a 10, las ventas de agosto 2025, los dulces vendidos en oct-dic 2025, las ventas por categoria y los productos en lista.
    print("\n" + "="*60)
    print("📊 ESTADÍSTICAS GENERALES".center(60))
    print("="*60)
    mostrar_estadisticas_generales(ventas)
#Productos con ventas menores a 10: se filtran los productos con ventas menores a
    print("\n" + "="*60)
    print("📉 PRODUCTOS CON VENTAS < $10".center(60))
    print("="*60)
    filtrar_poco_vendidos(ventas)
#Ventas por fecha: se filtran las ventas de agosto 2025.
    print("\n" + "="*60)
    print("📅 VENTAS DE AGOSTO 2025".center(60))
    print("="*60)
    filtrar_por_fecha(ventas, mes=8, anio=2025)
    graficar_ventas_por_fecha(ventas, mes=8, anio=2025) 
#Filtrar dulces vendidos en oct-dic 2025: se filtran los dulces vendidos en octubre a diciembre de 2025.
    print("\n" + "="*60)
    print("🍬 DULCES VENDIDOS EN OCT-DIC 2025".center(60))
    print("="*60)
    filtrar_dulces_oct_dic(ventas)
    graficar_dulces_oct_dic(ventas)
#Ventas por categoría: se muestran las ventas por categoría y se muestran los productos en lista.
    print("\n" + "="*60)
    print("📂 VENTAS POR CATEGORÍA".center(60))
    print("="*60)
    mostrar_ventas_por_categoria(ventas)
    ventas_por_categoria(ventas)
    graficar_ventas_por_categoria(ventas)
#Mostrar lista de productos con sus detalles: se convierte a lista de productos y se muestran los primeros 5 productos.
    print("\n" + "="*60)
    print("🛒 PRODUCTOS EN LISTA".center(60))
    print("="*60)
    print(f"{'Nombre del producto':<25} {'Precio':>10} {'Unidades':>10} {'Total Venta ($)':>17}")
    print("-" * 65)
    for producto in lista_productos[:5]:  # Muestra solo los primeros 5 productos
        print(f"{producto.nombre:<25} {producto.precio:>10.2f} {producto.unidades:>10} {producto.total_venta():>17.2f}")

    return lista_productos


if __name__ == "__main__":
    ventas = cargar_datos('PF_GRUPO_01.csv')
    ventas = procesar_datos(ventas)

    # Mostrar tuplas (categorías y fechas únicas)
    categorias_unicas = tuple(ventas["Categoría"].unique())
    fechas_unicas = tuple(ventas["Fecha"].dt.date.unique())

    print("\n" + "="*60)
    print("📂 CATEGORÍAS DISPONIBLES (Tupla)".center(60))
    print("="*60)
    print(categorias_unicas)

    print("\n" + "="*60)
    print("📅 FECHAS REGISTRADAS (Tupla)".center(60))
    print("="*60)
    fechas_formateadas = [fecha.strftime('%d/%m/%Y') for fecha in fechas_unicas]
    print(", ".join(fechas_formateadas))


    lista_productos = generar_resultados(ventas)
    contar_productos_por_categoria(lista_productos)
