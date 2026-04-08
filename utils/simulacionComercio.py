#funcion para generar N Medio de pago
#en spring boot el modelo de un servicio es: 
#id(Integer)
#nit(String)
#nombre(String)
#actividad(String)
#contacto(String)
#direccion(LocalDate)
#ciudad
#fechaRegistro
#estado
#tipoDeRegimen


import random
from datetime import datetime, timedelta
def simular_tabla_comercio(numeroServicios):
    #Defino atributo base
    nombre = ["dora", "la exploradora", "drax", "betto"]
    actividadEconomica = ["Agricultura", "Ganaderia", "Pesca", "Mineria"]
    nombreComercio = ["Panaderia", "Mcdonalds", "BURGER KING"]
    direccion = ["pescherman Cr 39 Cl wallace ", "cr 31 b 56a - 22", "PALMS Avenue"]
    ciudad = ["Maracaibo", "Barquisimento", "Medellin", "San Andres"]
    estado = [True, False]
    tipoDeRegimen = ["Regimen simplificado", "Regimen especial", "Regimen simple de tributacion"]



    #Para simular un rango de fecha debo introducir una fecha inicial
    fechaInicial = datetime(2010,1,1)
    fechaBase = fechaInicial+timedelta(days=random.randint(1,365))
    
    #ciclo para generar N registros de la tabla servicios
    servicios = []
    for _ in range (numeroServicios):
        servicio = {
            "id" : random.randint(1,1000),
            "nit" : str(random.randint(1000000, 1000000)),
            "nombre" : random.choice(nombre),
            "nombreDelComercio" : random.choice(nombreComercio),
            "actividad" : random.choice(actividadEconomica),
            "contacto" : random.randint(3000000000, 3300000000),
            "direccion" : random.choice(direccion),
            "fechaDeRegistro" : fechaBase.strftime("%Y/%m/%d"),
            "ciudad" : random.choice(ciudad),
            "estado" : random.choice(estado),
            "tipoDeRegimen" : random.choice(tipoDeRegimen)

        }

        servicios.append(servicio)
    return servicios