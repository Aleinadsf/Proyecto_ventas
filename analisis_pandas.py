import pandas as pd
from producto import Producto
# df = pd.read_csv("PF_GRUPO.csv")
# print(df.head())

# df["Fecha"] = pd.to_datetime(df["Fecha"])
# df["Total_Venta"] = df["Precio"] * df["Unidades vendidas"]

# ------se convirtio en funciones
# Estadísticas generales - Agregación
def mostrar_estadisticas_generales(df):
    print("\n--- Estadísticas Generales ---")
    print("Total de productos vendidos:", df["Unidades vendidas"].sum())
    print("Ingresos totales: S/.", df["Total_Venta"].sum())
    print("Precio promedio de productos: S/.", df["Precio"].mean())
    print("Producto más caro: S/.", df["Precio"].max())
    print("Producto más barato: S/.", df["Precio"].min())

# Filtrar productos que generaron menos de S/.10 en ventas
def filtrar_poco_vendidos(df):
    poco_vendidos = df[df["Total_Venta"] < 10]
    print("\n--- Productos con ventas menores a S/.10 ---")
    print(poco_vendidos[["Producto", "Total_Venta"]])


#Filtrar las ventas por fecha 
def filtrar_por_fecha(df, mes, anio):
    filtrado = df[(df["Fecha"].dt.month == mes) & (df["Fecha"].dt.year == anio)]
    print(f"\nVentas en {mes:02}/{anio}:")
    print(filtrado[["Fecha", "Producto", "Categoría", "Unidades vendidas", "Total_Venta"]])
    
    # agosto_2025 = df[df["Fecha"].dt.month == 8]
    # print("\nVentas en AGOSTO de 2025:")
    # print(agosto_2025[["Fecha", "Producto", "Categoría", "Unidades vendidas", "Total_Venta"]])


# Filtrar las categoría de producto
def ventas_por_categoria(df):
    totales = df.groupby("Categoría")["Total_Venta"].sum().sort_values(ascending=False)
    print("\n-------Ventas por categoría--------")
    print(totales)

def filtrar_dulces_oct_dic(df):
    dulces_oct_dic = df[
        (df["Categoría"] == "Dulces") &
        (df["Fecha"] >= "2025-10-01") &
        (df["Fecha"] <= "2025-12-31")
    ]
    print("\n------Ventas de DULCES entre OCT-DIC 2025-------")
    print(dulces_oct_dic[["Fecha", "Producto", "Unidades vendidas", "Total_Venta"]])

# dulces_oct_dic = df[
#     (df["Categoría"] == "Dulces") &
#     (df["Fecha"] >= "2025-10-01") &
#     (df["Fecha"] <= "2025-12-31")
# ]
# print("\nVentas de DULCES entre OCT-DIC 2025:")
# print(dulces_oct_dic[["Fecha", "Producto", "Unidades vendidas", "Total_Venta"]])
# Mostrar resumen total por categoría
# Agrupar
def mostrar_ventas_por_categoria(df):
    ventas_por_categoria = df.groupby("Categoría")["Total_Venta"].sum().sort_values(ascending=False)
    print("\n--- Ventas totales por categoría ---")
    print(ventas_por_categoria)
    
# ---------Listas 
def convertir_a_lista_productos(df):
    lista_productos = []
    for _, fila in df.iterrows():
        producto = Producto(
            id=fila["ID"],
            nombre=fila["Producto"],
            categoria=fila["Categoría"],
            fecha=fila["Fecha"],
            precio=fila["Precio"],
            unidades=fila["Unidades vendidas"]
        )
        lista_productos.append(producto)
    return lista_productos

def contar_productos_por_categoria(lista_productos):
    conteo = {}
    for producto in lista_productos:
        categoria = producto.categoria
        if categoria in conteo:
            conteo[categoria] += 1
        else:
            conteo[categoria] = 1

    print("\n--- Cantidad de productos por categoría ---")
    for categoria, cantidad in conteo.items():
        print(f"{categoria}: {cantidad}")
