import pandas as pd
def limpiar_datos_categoria(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()
    
    #procesando los textos del DATAFRAME sucio
    #limpiando los textos para eliminar espacios y mayusculas
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].astype("string").str.strip().str.lower()#str
    data_frame_limpio["responsable"] = data_frame_limpio["responsable"].astype("string").str.strip().str.lower()
    data_frame_limpio["justificacion"] = data_frame_limpio["justificacion"].astype("string").str.strip().str.lower()
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].astype("string").str.strip().str.lower()
    data_frame_limpio["codigo"] = data_frame_limpio["codigo"].astype("string").str.strip().str.lower()
    data_frame_limpio["estado"] = data_frame_limpio["estado"].astype("string").str.strip().str.lower()
    
    #para datos booleanos aun no por falta de explicacion y sin uso de la IA
    #data_frame_limpio["estado"] = data_frame_limpio["estado"].astype("boolean")

    #2. limpiando los texto para controlar valores inesperados
    valores_esperado_estado = ["activo", "inactivo"]
    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(valores_esperado_estado), 
        pd.NA
    )

    valores_esperados_nombreCategoria= ["alimentacion",
    "transporte",
    "entretenimiento",
    "educacion",
    "tecnologia",
    "hogar"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(
        data_frame_limpio["nombre"].isin(valores_esperados_nombreCategoria),
        pd.NA
    )

    valores_esperados_responsable= ["juan perez", "maria gomez", "carlos lopez", "ana torres", "luis ramirez"]
    data_frame_limpio["responsable"]=data_frame_limpio["responsable"].where(
        data_frame_limpio["responsable"].isin(valores_esperados_responsable),
        pd.NA
    )
    
    valores_esperados_justificacion= ["necesidad basica", "uso frecuente", "obligatorio", "prevencion", "ocio"]
    data_frame_limpio["justificacion"]=data_frame_limpio["justificacion"].where(
        data_frame_limpio["justificacion"].isin(valores_esperados_justificacion),
        pd.NA
    )

    valores_esperados_descripcion= ["gastos mensuales", "costos diarios", "inversion anual", "chequeos medicos", "diversion"]
    data_frame_limpio["descripcion"]=data_frame_limpio["descripcion"].where(
        data_frame_limpio["descripcion"].isin(valores_esperados_descripcion),
        pd.NA
    )

    valores_esperados_codigo= ["z748", "f899", "t001", "g2025", "g788"]
    data_frame_limpio["codigo"]=data_frame_limpio["codigo"].where(
        data_frame_limpio["codigo"].isin(valores_esperados_codigo),
        pd.NA
    )


    #1.1 limpieza de datos numericos verficamos que los datos sean numericos
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])

    #1.2 verificamoslos valores esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"]>0]

    data_frame_limpio["fechaCreacion"] = pd.to_datetime(data_frame_limpio["fechaCreacion"])
    data_frame_limpio["fechaModificacion"] = pd.to_datetime(data_frame_limpio["fechaModificacion"])

    #limpieza por fecha verificamos si el campo es una fecha
    fecha_default = pd.to_datetime("2025-1-1")
    data_frame_limpio["fechaCreacion"] = data_frame_limpio["fechaCreacion"].fillna(fecha_default)

    fecha_default = pd.to_datetime("2025-01-1")
    data_frame_limpio["fechaModificacion"] = data_frame_limpio["fechaModificacion"].fillna(fecha_default)


    #novedades de datos vacios
    columnas_obligatorias = ["id","nombre", "responsable", "justificacion","descripcion", "estado","codigo","fechaCreacion","fechaModificacion"]
    data_frame_limpio= data_frame_limpio.dropna(subset=columnas_obligatorias)


    #limpieza de datos booleanos
    #valores_esperados_estado=[True, False]
    #data_frame_limpio["estado"]=data_frame_limpio["estado"].where(
    #    data_frame_limpio["estado"].isin([True, False]), pd.NA)
    return data_frame_limpio