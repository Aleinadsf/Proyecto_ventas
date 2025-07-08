import pandas as pd

# Carga de datos y creacion de un  DataFrame desde el archivo CSV
datos = pd.read_csv("PF_GRUPO.csv")

# FILTRO POR CATEGORÍA
print("VENTAS AGRUPADAS POR CATEGORÍA")
categorias = datos["Categoría"].unique()

for cat in categorias:
    print(f"\nCategoría: {cat}")
    filtro_categoria = datos[datos["Categoría"] == cat]
    print(filtro_categoria)

# FILTRO POR FECHA
print("\nVENTAS AGRUPADAS POR FECHA")
fechas = datos["Fecha"].unique()

for fecha in fechas:
    print(f"\nFecha: {fecha}")
    filtro_fecha = datos[datos["Fecha"] == fecha]
    print(filtro_fecha)


# OPERACIONES DE AGREGACIÓN

# Suma de totales

print("TOTAL DE UNIDADES VENDIDAS POR CATEGORÍA:")
ventas_categoria = datos.groupby("Categoría")["Unidades vendidas"].sum()
for cat, total in ventas_categoria.items():
    print(f"El total de unidades vendidas de la categoría '{cat}' es: {total}")

print("TOTAL DE UNIDADES VENDIDAS POR PRODUCTO:")
ventas_producto = datos.groupby("Producto")["Unidades vendidas"].sum()
for prod, total in ventas_producto.items():
    print(f"El total de unidades vendidas del producto '{prod}' es: {total}")

# Promedio

print("PROMEDIO POR CATEGORÍA:")
promedio_categoria = datos.groupby("Categoría")["Unidades vendidas"].mean()
for cat, promedio in promedio_categoria.items():
    print(f"El promedio de unidades vendidas en la categoría '{cat}' es: {promedio:.2f}")

print("PROMEDIO  POR PRODUCTO:")
promedio_producto = datos.groupby("Producto")["Unidades vendidas"].mean()
for prod, promedio in promedio_producto.items():
    print(f"El promedio de unidades vendidas del producto '{prod}' es: {promedio:.2f}")
