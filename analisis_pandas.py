import pandas as pd
from producto import Producto
import matplotlib.pyplot as plt
import seaborn as sns

# ------se convirtio en funciones
# Estadísticas generales - Agregación
def mostrar_estadisticas_generales(df):
    print("Total de productos vendidos:", df["Unidades vendidas"].sum())
    print(f"Ingresos totales: S/. {df['Total_Venta'].sum():.2f}")
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

#grafico de barras - total de ventas por categoría
def graficar_ventas_por_categoria(df):
    resumen = df.groupby("Categoría")["Total_Venta"].sum().sort_values()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=resumen.values, y=resumen.index, color="skyblue")  
    plt.title("Ventas Totales por Categoría")
    plt.xlabel("Total de Ventas (S/.)")
    plt.ylabel("Categoría")
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

def graficar_ventas_por_fecha(df, mes, anio):
    df_filtrado = df[(df["Fecha"].dt.month == mes) & (df["Fecha"].dt.year == anio)]
    resumen = df_filtrado.groupby(df_filtrado["Fecha"].dt.day)["Total_Venta"].sum()

    plt.figure(figsize=(10, 5))
    resumen.plot(kind="bar", color="skyblue")
    plt.title(f"Ventas por Día - {mes:02}/{anio}")
    plt.xlabel("Día del mes")
    plt.ylabel("Total de Ventas (S/.)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def graficar_dulces_oct_dic(df):
    df_dulces = df[
        (df["Categoría"] == "Dulces") &
        (df["Fecha"] >= "2025-10-01") &
        (df["Fecha"] <= "2025-12-31")
    ]
    resumen = df_dulces.groupby(df_dulces["Fecha"].dt.date)["Total_Venta"].sum()

    plt.figure(figsize=(10, 5))
    resumen.plot(kind="line", marker="o", color="orchid")
    plt.title("Ventas de Dulces (Oct-Dic 2025)")
    plt.xlabel("Fecha")
    plt.ylabel("Total de Ventas (S/.)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
