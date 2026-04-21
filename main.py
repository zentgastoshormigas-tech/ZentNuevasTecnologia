import pandas as pd
from utils.simulacionCategoria import simular_tabla_categoria
from notebook.generador import crear_json, crear_csv

simulacionDeCategoria = simular_tabla_categoria(10)
simulacionOrdenadaDeCategoria = pd.DataFrame(simulacionDeCategoria)

crear_json(simulacionOrdenadaDeCategoria, "data/datosCategoria.json")
crear_csv(simulacionOrdenadaDeCategoria, "data/datosCategoria.csv")
