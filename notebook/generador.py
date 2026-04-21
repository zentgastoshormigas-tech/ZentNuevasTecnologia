import pandas as pd

def crear_json(data_frame, nombre_archivo):
    data_frame.to_json(nombre_archivo, orient="records", indent=4)


def crear_csv(dataframe, nombre_archivo):
    dataframe.to_csv(nombre_archivo, index=False)