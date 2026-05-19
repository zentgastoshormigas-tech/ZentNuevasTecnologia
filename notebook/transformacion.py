import pandas as pd

def transformar_datos_categoria(data_frame_limpio):
    filtro_uno = data_frame_limpio.query("nombre=='alimentacion'")
    agrupacion=filtro_uno.groupby("responsable")["id"].count().reset_index(name="cuenta")

    filtro_dos = data_frame_limpio.query("codigo=='g2025'")
    agrupacion_dos = filtro_dos.groupby("nombre")["id"].count().reset_index(name="cuenta")

    resultado = {
        "agrupacion": agrupacion,
        "agrupacion_por_nombre": agrupacion_dos
    }

    return resultado