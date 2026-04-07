#funcion para generar N Gastos
#en springboot el modelo de Gasto
#id(int)
#descrpcion(String),
#fechaRegistro(LocalDate),
#valor(double),
#imagen(String),
#categoria(String),
#estado(Boolean), 
#usuario(String),
#comercio(String)
import random
from datetime import datetime, timedelta

def simular_tabla_gasto(numeroUsuarios):
    #Defino atributo base
    usuario = input("ingrese nombre del usuario que hara los gastos")
    categoria = ["Alimentos", "Transporte", "Entretenimiento", "Educacion", "Tecnologia", "Hogar"]
    responsable = [usuario]
    justificacion = ["era necesario", "no tenia efectivo", "no tenian cambio en efectivo", "solo queria" ]
    descripcion = ["descripcion al azar", "descripcion al azar 1", "descripcion al azar 2", "descripcion al azar 3"]
    url = ["pinteres.png", "www.amazon.png", "www.marketplace.com"]
    comercio =["Mcdonal", "Pizza hut", "Dominos Pizza", "Burger king", "Exito"]
    
    
    #anios = [2000, 1999, 1998, 2001]
    #aniosRegistro = [2018, 2019, 2020, 2021]
    estado = [True, False]

    #anio = random.choice(anios)
    #aniosRegistro = random.choice(aniosRegistro)



    #Para simular un rango de fecha debo introducir una fecha inicial
    #fechaInicial = datetime(2026,1,1)
    #fechaBase = fechaInicial+timedelta(days=random.randint(0,365))
    
    #ciclo para generar N registros de la tabla servicios
    servicios = []
    for _ in range (numeroUsuarios):
        
            fechaInicialAnios = datetime(2026, 1, 1)
            fechaBaseAnio = fechaInicialAnios + timedelta(days=random.randint(1, 210))

            #fechaModificacion = datetime(2026, 1, 1)
            #fechaBaseModificacion = fechaModificacion + timedelta(days=random.randint(1, 365))


            servicio = {
                "id" : random.randint(1,1000),
                "Descripcion" : random.choice(justificacion),
                "fechaDeRegistro" : fechaBaseAnio.strftime("%Y/%m/%d"),
                "valor" : random.randint(1, 1000000),
                "imagen" : random.choice(url),
                "categoria" : random.choice(categoria),
                "responsable" : responsable,
                "justificacion" : random.choice(justificacion),
                "descripcion" : random.choice(descripcion),
                "estado" : random.choice(estado),
                "comercio" : random.choice(comercio)
            }

            servicios.append(servicio)
    return servicios