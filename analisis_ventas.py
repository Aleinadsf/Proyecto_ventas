import pandas as pd

# Carga de datos y creacion de un  DataFrame desde el archivo CSV
datos = pd.read_csv("PF_GRUPO.csv")

# FILTRO POR CATEGORÍA
print(" VENTAS AGRUPADAS POR CATEGORÍA")
categorias = datos["Categoría"].unique()

for cat in categorias:
    print(f"Categoría: {cat}")
    filtro_categoria = datos[datos["Categoría"] == cat]
    print(filtro_categoria)
    print("-" * 40)

# FILTRO POR FECHA
print("VENTAS AGRUPADAS POR FECHA")
fechas = datos["Fecha"].unique()

for fecha in fechas:
    print(f"Fecha: {fecha}")
    filtro_fecha = datos[datos["Fecha"] == fecha]
    print(filtro_fecha)
    print("-" * 40)

# OPERACIONES DE AGREGACIÓN

# suma las ventas por categoría 
print("Total de unidades por CATEGORÍA:")
ventas_categoria = datos.groupby("Categoría")["Unidades vendidas"].sum()
print(ventas_categoria)
print("-" * 40)

# suma las ventas por producto 
print("Total de unidades por PRODUCTO:")
ventas_producto = datos.groupby("Producto")["Unidades vendidas"].sum()
print(ventas_producto)
print("-" * 40)

# Calcular total
datos["Total"] = datos["Precio"] * datos["Unidades vendidas"]

# Total de ingresos por categoría
print("Ingresos por CATEGORÍA:")
ingresos_categoria = datos.groupby("Categoría")["Total"].sum()
print(ingresos_categoria)
print("-" * 40)

# Total de ingresos por producto
print("Ingresos por PRODUCTO:")
ingresos_producto = datos.groupby("Producto")["Total"].sum()
print(ingresos_producto)
print("-" * 40)


# Promedio de unidades por categorías
print("Promedio de unidades por categoría:")
print(datos.groupby("Categoría")["Unidades vendidas"].mean())
print("-" * 40)