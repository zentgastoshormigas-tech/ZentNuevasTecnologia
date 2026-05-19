#importa simulaciones

#from utils.simulacionCategoria import simular_tabla_categoria

#zona limpieza
#from notebook.limpiezaCategoria import limpiar_datos_categoria

#importa generador de json y csv
#from notebook.generador import crear_csv, crear_json

#importar descripcion de los datos obtenidos
#from notebook.descripcion import describir_datos

#crear simulacion
#simulacionDeCategoria = simular_tabla_categoria(1000)
#ordenando simulaciones
#simulacionOrdenadaDeCategoria = pd.DataFrame(simulacionDeCategoria)


#limpiar set de datos
#simulaciones_limpias_categoria = limpiar_datos_categoria(simulacionOrdenadaDeCategoria)

#describiendo datos
#describir_datos(simulaciones_limpias_categoria)

import pandas as pd

from notebook.consumo import consumir_api_zend

from notebook.limpiezaCategoria import limpiar_datos_categoria

from notebook.transformacion import transformar_datos_categoria


datos = consumir_api_zend()

data_frame_datos_categoria = pd.DataFrame(datos)

limpieza_datos_categoria = limpiar_datos_categoria(data_frame_datos_categoria)

resultado_de_transformacion = transformar_datos_categoria(limpieza_datos_categoria)

print(resultado_de_transformacion)