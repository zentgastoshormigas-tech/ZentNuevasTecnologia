import pandas as pd

def transformar_datos_gasto(data_frame_limpio):
    primer_filtro = data_frame_limpio.query("valor>=20000")
    grupo=primer_filtro.groupby("responsable")["id"].count().reset_index(name="conteo")

    segundo_filtro = data_frame_limpio.query("valor<=20000")
    grupo_dos = segundo_filtro.groupby("responsable")["id"].count().reset_index(name="conteo")

    resultado = {
        "grupo": grupo,
        "grupo_dos": grupo_dos
    }

    return resultado