
# 🧁 Proyecto de Análisis de Ventas – Pastelería

## Descripción del proyecto

Este proyecto consiste en el diseño de un programa en **Python** que analiza un conjunto de datos simulados de ventas en una pastelería. El programa permite:

✔ Cargar los datos desde un archivo **CSV**.
✔ Filtrar ventas por fecha o categoría.
✔ Calcular estadísticas generales con **Pandas** y análisis estadístico con **NumPy**.
✔ Mostrar los resultados de manera organizada en consola.
✔ Convertir los datos en **objetos** mediante una clase `Producto`.
✔ Utilizar estructuras de datos como **listas, tuplas y diccionarios**.

Este proyecto cumple con los requerimientos de:

* **Estructuras repetitivas** y uso de listas.
* **Funciones y módulos** para una estructura ordenada.
* **Clases y objetos** para modelar las ventas.
* Uso de **Pandas** para manipulación de datos.
* Uso de **NumPy** para cálculos estadísticos.
* **Documentación clara** y presentación profesional.


## Estructura del proyecto

Proyecto_ventas/
│
├── PF_GRUPO.csv             
├── main.py                  
├── producto.py              
├── analisis_pandas.py       
├── analisis_numpy.py        
├── utils.py                 
├── README.md                
└── __pycache__/  



## **Requisitos previos**

Asegúrate de tener instalado:

* **Python 3.8 o superior**
* Librerías externas:
  * `pandas`
  * `numpy`

Instala las dependencias con:

- pip install pandas numpy

## ▶ **Ejecución del programa**

Desde la raíz del proyecto, ejecuta:

- python main.py

## Funcionalidades principales

1. Carga y limpieza de datos

   * Se cargan los datos desde `PF_GRUPO.csv` usando Pandas.
   * Se agrega la columna `Total_Venta` calculada como `Precio * Unidades vendidas`.

2. Estadísticas generales (Pandas)

   * Total de productos vendidos.
   * Ingresos totales.
   * Precio promedio.
   * Producto más caro y más barato.

3. Estadísticas avanzadas (NumPy)

   * Promedio de ventas.
   * Desviación estándar.
   * Mediana, mínimo y máximo.

4. Filtros dinámicos

   * Ventas por categoría.
   * Ventas en un mes específico (ej. agosto 2025).
   * Ventas de dulces entre octubre y diciembre 2025.
   * Productos con ventas menores a S/.10.

5. Estructuras solicitadas

   * **Listas** → Conversión del DataFrame a lista de objetos `Producto`.
   * **Tuplas** → Categorías únicas y fechas únicas.
   * **Diccionarios** → Conteo de productos por categoría.


## 🧾 Ejemplo de salida en consola


============================================================
📂 CATEGORÍAS DISPONIBLES (Tupla)
============================================================
('Dulces', 'Bebidas', 'Pasteles', 'Galletas')

============================================================
📅 FECHAS REGISTRADAS (Tupla)
============================================================
(datetime.date(2025, 8, 1), datetime.date(2025, 8, 15), ...)

============================================================
🔍 ANÁLISIS ESTADÍSTICOS DE LAS VENTAS
============================================================
Promedio            : 27.35
Desviacion_estandar : 15.42
Mediana             : 26.50
Minimo              : 5.00
Maximo              : 120.00

...


## 👨‍💻 Autores

Moreno Medina, Krystel Victoria - U22214055
Suarez Franklin, Daniela Nayeli - U22215095
Aquijes Rivera, Maricielo Victoria - U22229709


* Curso: Lenguaje de programacion
* Fecha: Julio,2025


