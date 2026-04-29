import pandas as pd

#importa simulaciones

from utils.simulacionCategoria import simular_tabla_categoria

#zona limpieza
from notebook.limpiezaCategoria import limpiar_datos_categoria

#importa generador de json y csv
from notebook.generador import crear_csv, crear_json

#crear simulacion
simulacionDeCategoria = simular_tabla_categoria(1000)
#ordenando simulaciones
simulacionOrdenadaDeCategoria = pd.DataFrame(simulacionDeCategoria)


#limpiar set de datos
simulaciones_limpias_categoria = limpiar_datos_categoria(simulacionOrdenadaDeCategoria)
print(simulaciones_limpias_categoria)


crear_json(simulaciones_limpias_categoria, "data/datosCategoria.json")
crear_csv(simulaciones_limpias_categoria, "data/datosCategoria.csv")
