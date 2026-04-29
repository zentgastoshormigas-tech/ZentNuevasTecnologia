import pandas as pd
import random

def limpiar_datos_usuario(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy() #method copy() copiamos el dataframe_sucio por cualquier tipo de error no arruinar la principal

    #copiamos el dataframe_sucio por cualquier tipo de error no arruinar la principal


#procesando los textos del DATAFRAME sucio
#limpiando los textos para eliminar espacios y mayusculas
    data_frame_limpio["nombres"] = data_frame_limpio["nombres"].astype("string").str.strip().str.lower()#str
    data_frame_limpio["tipoDeDocumento"] = data_frame_limpio["tipoDeDocumento"].astype("string").str.strip().str.lower()
    data_frame_limpio["documento"] = data_frame_limpio["documento"].astype("string").str.strip().str.lower()
    data_frame_limpio["correo"] = data_frame_limpio["correo"].astype("string").str.strip().str.lower()
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].astype("string").str.strip().str.lower()
    
    #para datos booleanos aun no por falta de explicacion y sin uso de la IA
    #data_frame_limpio["estado"] = data_frame_limpio["estado"].astype("boolean")

    #2. limpiando los texto para controlar valores inesperados
    valores_esperados_nombre= ["Julio", "Cesar", "Joshua", "Karin", "Leo"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(
        data_frame_limpio["nombre"].isin(valores_esperados_nombre),
        pd.NA
    )

    valores_esperados_tipoDeDocumento= ["Cedula", "Tarjeta de Identidad", "Registro Civil", "Pasaporte"]
    data_frame_limpio["tipoDeDocumento"]=data_frame_limpio["tipoDeDocumento"].where(
        data_frame_limpio["tipoDeDocumento"].isin(valores_esperados_tipoDeDocumento),
        pd.NA
    )
    
    valores_esperados_documento= str(random.randint(100, 1000) for _ in range(10))
    data_frame_limpio["documento"]=data_frame_limpio["documento"].where(
        data_frame_limpio["documento"].isin(valores_esperados_documento),
        pd.NA
    )

    valores_esperados_correo= ["fulanito@gmail.com", "pancho@gmail.com", "pedro@gmail.com", "jesus@gmail.com"]
    data_frame_limpio["correo"]=data_frame_limpio["correo"].where(
        data_frame_limpio["correo"].isin(valores_esperados_correo),
        pd.NA
    )

    valores_esperados_telefono= str(random.randint(3000000000, 3100000000) for _ in range(10))
    data_frame_limpio["telefono"]=data_frame_limpio["telefono"].where(
        data_frame_limpio["telefono"].isin(valores_esperados_telefono),
        pd.NA
    )


    


    #1.1 limpieza de datos numericos verficamos que los datos sean numericos
    data_frame_limpio["edad"] = pd.to_numeric(data_frame_limpio["edad"])
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])

    #1.2 verificamoslos valores esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["edad"]>17]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"]>0]

    #limpieza por fecha verificamos si el campo es una fecha
    fecha_default = pd.to_datetime("1998-01-01")
    data_frame_limpio["fechaDeNacimiento"] = data_frame_limpio["fechaDeNacimiento"].fillna(fecha_default)

    fecha_default = pd.to_datetime("2018-01-01")
    data_frame_limpio["fechaDeRegistro"] = data_frame_limpio["fechaDeRegistro"].fillna(fecha_default)


    #novedades de datos vacios
    columnas_obligatorias = ["id","nombres", "tipoDeDocumento", "documento","correo", "telefono","id","edad", "fechaDeNacimiento", "fechaDeRegistro"]
    data_frame_limpio= data_frame_limpio.dropna(subset=columnas_obligatorias)




    #limpieza de datos booleanos
    #valores_esperados_estado=[True, False]
    #data_frame_limpio["estado"]=data_frame_limpio["estado"].where(
    #    data_frame_limpio["estado"].isin([True, False]), pd.NA)
    return data_frame_limpio







def limpiar_datos_medio_de_pago(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #modelo medio de pago va aqui



def limpiar_datos_gasto(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

   #procesando los textos del DATAFRAME sucio
    #limpiando los textos para eliminar espacios y mayusculas
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].astype("string").str.strip().str.lower()
    data_frame_limpio["categoria"] = data_frame_limpio["categoria"].astype("string").str.strip().str.lower()
    data_frame_limpio["responsable"] = data_frame_limpio["responsable"].astype("string").str.strip().str.lower()
    data_frame_limpio["justificacion"] = data_frame_limpio["justificacion"].astype("string").str.strip().str.lower()
    data_frame_limpio["comercio"] = data_frame_limpio["comercio"].astype("string").str.strip().str.lower()

    #2. limpiando los textos para controlar valores inesperados
    valores_esperados_descripcion=["descripcion al azar", "descripcion al azar 1", "descripcion al azar 2", "descripcion al azar 3"]
    data_frame_limpio["descripcion"]=data_frame_limpio["descripcion"].where(
        data_frame_limpio["descripcion"].isin(valores_esperados_descripcion),
        pd.NA
    ) 

    valores_esperados_categoria=["Alimentos", "Transporte", "Entretenimiento", "Educacion", "Tecnologia", "Hogar"]
    data_frame_limpio["categoria"]=data_frame_limpio["categoria"].where(
        data_frame_limpio["categoria"].isin(valores_esperados_categoria),
        pd.NA
    ) 

    valores_esperados_responsable=["Usuario1", "Usuario2", "usuario3"]
    data_frame_limpio["responsable"]=data_frame_limpio["responsable"].where(
        data_frame_limpio["responsable"].isin(valores_esperados_responsable),
        pd.NA
    ) 

    valores_esperados_justificacion=["era necesario", "no tenia efectivo", "no tenian cambio en efectivo", "solo queria"]
    data_frame_limpio["justificacion"]=data_frame_limpio["justificacion"].where(
        data_frame_limpio["justificacion"].isin(valores_esperados_justificacion),
        pd.NA
    ) 

    valores_esperados_comercio=["era necesario", "no tenia efectivo", "no tenian cambio en efectivo", "solo queria"]
    data_frame_limpio["comercio"]=data_frame_limpio["comercio"].where(
        data_frame_limpio["comercio"].isin(valores_esperados_comercio),
        pd.NA
    ) 

     #3. Limpieza de datos numericos

    #1. verificar que los numeros si sean numeros

    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    
    data_frame_limpio["valor"]=pd.to_numeric(data_frame_limpio["valor"])

    #2. verifiquemos los valores numericos esperados
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"]>0)
    data_frame_limpio["valor"] = pd.to_numeric(data_frame_limpio["valor"]>0)

    #1. Limpieza de fechas
    #1. verficar que el campo si es una fecha
    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio["fechaRegistro"] = data_frame_limpio["fechaRegistro"].fillna(fecha_default)

    #Novedades de datos vacios
    columnas_obligatorias=["id", "valor", "fechaRegistro", "comercio", "justificacion", "responsable", "categoria", "descripcion"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio
    


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