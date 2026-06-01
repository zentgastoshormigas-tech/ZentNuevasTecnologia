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

from notebook.limpieza import limpiar_datos_gasto

from notebook.transformacion import transformar_datos_categoria

from notebook.transformacion_gasto import transformar_datos_gasto

from notebook.graficacion import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor


datos = consumir_api_zend()

data_frame_datos_categoria = pd.DataFrame(datos)
data_frame_datos_gasto = pd.DataFrame(datos)

limpieza_datos_categoria = limpiar_datos_categoria(data_frame_datos_categoria)
limpieza_datos_gasto = limpiar_datos_gasto(data_frame_datos_gasto)

resultado_de_transformacion_gasto = transformar_datos_gasto(limpieza_datos_gasto)
resultado_de_transformacion_categoria = transformar_datos_categoria(limpieza_datos_categoria)

agrupaciones=transformar_datos_categoria(resultado_de_transformacion_categoria)
agrupaciones_dos = transformar_datos_gasto(resultado_de_transformacion_gasto)
# Gráfico de líneas:  por valor superior a 20000
graficar_lineas(
    agrupaciones["grupo"],
    columna_eje_x="responsable",
    columna_eje_y="conteo",
    titulo="agrupacion de valores superiores a 20000",
    color_linea="#2196F3",
    nombre_archivo="lineas_por_valores_superiores_a_20000.png"
)

# Gráfico de barras: por valores inferiores a 20000
graficar_barras(
    agrupaciones["grupo_dos"],
    columna_categorias="responsable",
    columna_valores="conteo",
    titulo="agrupacion de valores inferiores a 20000",
    color_barras="#4CAF50",
    nombre_archivo="barras_valroes_inferiores_A_20000.png"
)

# Gráfico de torta: se agrupa por nombre de categoria
graficar_torta(
    agrupaciones["agrupacion"],
    columna_etiquetas="responsable",
    columna_valores="conteo",
    titulo="se agrupa por nombre de categoria",
    nombre_archivo="torta_nombre_por_categoria.png"
)

# Mapa de calor: cantidad de nombre de categoria por codigo
graficar_mapa_calor(
    agrupaciones["agrupacion_por_nombre"],
    columna_filas="nombre",
    columna_columnas="codigo",
    columna_valores="conteo",
    titulo="Cantidad de nombre por codigo",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_nombre_De_categoria.png"
)