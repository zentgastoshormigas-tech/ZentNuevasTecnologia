import pandas as pd
import random

def limpiar_datos_usuario(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy() #method copy() copiamos el dataframe_sucio por cualquier tipo de error no arruinar la principal

    #modelo usuario va aqui







def limpiar_datos_medio_de_pago(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #modelo medio de pago va aqui



def limpiar_datos_gasto(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #modelo gasto va aqui
    


def limpiar_datos_comercio(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #modelo comercio va aqui





def limpiar_datos_categoria(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()
    
    #procesando los textos del DATAFRAME sucio
    #limpiando los textos para eliminar espacios y mayusculas
    data_frame_limpio["nombresCategoria"] = data_frame_limpio["nombreCategoria"].astype("string").str.strip().str.lower()#str
    data_frame_limpio["responsable"] = data_frame_limpio["responsable"].astype("string").str.strip().str.lower()
    data_frame_limpio["justificacion"] = data_frame_limpio["justificacion"].astype("string").str.strip().str.lower()
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].astype("string").str.strip().str.lower()
    data_frame_limpio["codigo"] = data_frame_limpio["codigo"].astype("string").str.strip().str.lower()
    
    #para datos booleanos aun no por falta de explicacion y sin uso de la IA
    #data_frame_limpio["estado"] = data_frame_limpio["estado"].astype("boolean")

    #2. limpiando los texto para controlar valores inesperados
    valores_esperados_nombreCategoria= ["Alimentos", "Transporte", "Entretenimiento", "Educacion", "Tecnologia", "Hogar"]
    data_frame_limpio["nombreCategoria"]=data_frame_limpio["nombreCategoria"].where(
        data_frame_limpio["nombreCategoria"].isin(valores_esperados_nombreCategoria),
        pd.NA
    )

    valores_esperados_responsable= ["elpietro", "albaro", "julio", "cesar"]
    data_frame_limpio["responsable"]=data_frame_limpio["responsable"].where(
        data_frame_limpio["responsable"].isin(valores_esperados_responsable),
        pd.NA
    )
    
    valores_esperados_justificacion= ["era necesario", "no tenia efectivo", "no tenian cambio en efectivo", "solo queria"]
    data_frame_limpio["justificacion"]=data_frame_limpio["justificacion"].where(
        data_frame_limpio["justificacion"].isin(valores_esperados_justificacion),
        pd.NA
    )

    valores_esperados_descripcion= ["descripcion al azar", "descripcion al azar 1", "descripcion al azar 2", "descripcion al azar 3"]
    data_frame_limpio["descripcion"]=data_frame_limpio["descripcion"].where(
        data_frame_limpio["descripcion"].isin(valores_esperados_descripcion),
        pd.NA
    )

    valores_esperados_codigo= ["Z748", "F899", "T001", "G2025", "V788"]
    data_frame_limpio["codigo"]=data_frame_limpio["codigo"].where(
        data_frame_limpio["codigo"].isin(valores_esperados_codigo),
        pd.NA
    )


    #1.1 limpieza de datos numericos verficamos que los datos sean numericos
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])

    #1.2 verificamoslos valores esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"]>0]

    #limpieza por fecha verificamos si el campo es una fecha
    fecha_default = pd.to_datetime("2025, 1, 1")
    data_frame_limpio["fechaDeCreacion"] = data_frame_limpio["fechaDeCreacion"].fillna(fecha_default)

    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio["fechaModificacion"] = data_frame_limpio["fechaModificacion"].fillna(fecha_default)


    #novedades de datos vacios
    columnas_obligatorias = ["id","nombresCategoria", "responsable", "justificacion","descripcion", "codigo","fechaDeCreacion","fechaModificacion"]
    data_frame_limpio= data_frame_limpio.dropna(subset=columnas_obligatorias)


    #limpieza de datos booleanos
    #valores_esperados_estado=[True, False]
    #data_frame_limpio["estado"]=data_frame_limpio["estado"].where(
    #    data_frame_limpio["estado"].isin([True, False]), pd.NA)
    return data_frame_limpio