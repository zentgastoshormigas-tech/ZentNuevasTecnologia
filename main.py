import pandas as pd

#importa simulaciones
from utils.simulacionCategoria import simular_tabla_categoria

#zona limpieza
from notebook.limpieza import limpiar_datos_categoria

#importa generador de json y csv
from notebook.generador import crear_json, crear_csv


#crear simulacion
simulacionDeCategoria = simular_tabla_categoria(10)
#ordenando simulaciones
simulacionOrdenadaDeCategoria = pd.DataFrame(simulacionDeCategoria)

#limpiar set de datos
simulaciones_limpias_categoria = limpiar_datos_categoria(simulacionOrdenadaDeCategoria)


crear_json(simulaciones_limpias_categoria, "data/datosCategoria.json")
crear_csv(simulaciones_limpias_categoria, "data/datosCategoria.csv")
