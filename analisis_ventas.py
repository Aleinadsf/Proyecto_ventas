import pandas as pd

df = pd.read_csv("PF_GRUPO.csv")
print(df.head())

df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Total_Venta"] = df["Precio"] * df["Unidades vendidas"]


# Estadísticas generales - Agregación
print("\n--- Estadísticas Generales ---")
print("Total de productos vendidos:", df["Unidades vendidas"].sum())
print("Ingresos totales: $", df["Total_Venta"].sum())
print("Precio promedio de productos: $", df["Precio"].mean())
print("Producto más caro: $", df["Precio"].max())
print("Producto más barato: $", df["Precio"].min())

# Filtrar productos que generaron menos de $10 en ventas
poco_vendidos = df[df["Total_Venta"] < 10]
print("\n--- Productos con ventas menores a $10 ---")
print(poco_vendidos[["Producto", "Total_Venta"]])


#Filtrar las ventas por fecha 
agosto_2025 = df[df["Fecha"].dt.month == 8]
print("\nVentas en AGOSTO de 2025:")
print(agosto_2025[["Fecha", "Producto", "Categoría", "Unidades vendidas", "Total_Venta"]])


# Filtrar las categoría de producto
dulces_oct_dic = df[
    (df["Categoría"] == "Dulces") &
    (df["Fecha"] >= "2025-10-01") &
    (df["Fecha"] <= "2025-12-31")
]
print("\nVentas de DULCES entre OCT-DIC 2025:")
print(dulces_oct_dic[["Fecha", "Producto", "Unidades vendidas", "Total_Venta"]])

# Agrupar 
ventas_por_categoria = df.groupby("Categoría")["Total_Venta"].sum().sort_values(ascending=False)
print("\n--- Ventas totales por categoría ---")
print(ventas_por_categoria)

ventas_por_categoria.to_csv("ventas_por_categoria.csv")
poco_vendidos.to_csv("productos_poco_vendidos.csv", index=False)