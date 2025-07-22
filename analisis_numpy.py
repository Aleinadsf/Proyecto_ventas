import numpy as np

# funcion para calcular estadisticas
def calcular_estadisticas(ventas_np):
    return{
        "promedio": np.mean(ventas_np),
        "desviacion_estandar": np.std(ventas_np),
        "mediana": np.median(ventas_np),
        "minimo": np.min(ventas_np),
        "maximo": np.max(ventas_np)
    }
