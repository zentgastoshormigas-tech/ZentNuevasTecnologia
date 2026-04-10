#funcion para generar N usuarios
#en springboot el modelo de Usuario
#id(int)
#nombre(String),
#tipoDocumento(TipoDocumento),
#documento(int),
#correo(String),
#fechaNacimiento(localDate),
#telefono(String), 
#fechaRegistro(LocalDate),
#estado(Boolean)
import random
from datetime import datetime, timedelta

def simular_tabla_usuario(numeroUsuarios):
    #Defino atributo base
    nombres = ["Julio", "Cesar", "Joshua", "Karin", "Leo"]
    tipoDeDocumento = ["Cedula", "Tarjeta de Identidad", "Registro Civil", "Pasaporte"]
    correo = ["fulanito@gmail.com", "pancho@gmail.com", "pedro@gmail.com", "jesus@gmail.com"]
    anios = [2000, 1999, 1998, 2001]
    aniosRegistro = [2018, 2019, 2020, 2021]
    estado = [True, False]

    anio = random.choice(anios)
    aniosRegistro = random.choice(aniosRegistro)



    #Para simular un rango de fecha debo introducir una fecha inicial
    #fechaInicial = datetime(2026,1,1)
    #fechaBase = fechaInicial+timedelta(days=random.randint(0,365))
    
    #ciclo para generar N registros de la tabla servicios
    servicios = []
    for _ in range (numeroUsuarios):
        
            fechaInicialAnios = datetime(anio, 1, 1)
            fechaBaseAnio = fechaInicialAnios + timedelta(days=random.randint(1, 365))

            fechaInicialRegistro = datetime(aniosRegistro, 1, 1)
            fechaBaseRegistro = fechaInicialRegistro + timedelta(days=random.randint(1, 365))


            servicio = {
                "id" : random.randint(1,1000),
                "Nombre" : random.choice(nombres),
                "tipoDeDocumento" : random.choice(tipoDeDocumento),
                "documento" : str(random.randint(100, 1000)),
                "edad" : random.randint(1, 85),
                "correo" : random.choice(correo),
                "fechaDeNacimiento" : fechaBaseAnio.strftime("%Y/%m/%d"),
                "telefono" : str(random.randint(3000000000, 3999999999)),
                "fechaDeRegistro" : fechaBaseRegistro.strftime("%Y/%m/%d"),
                "estado" : random.choice(estado)
            }

            servicios.append(servicio)
    return servicios