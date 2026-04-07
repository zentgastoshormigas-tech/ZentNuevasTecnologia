#funcion para generar N categoria
#en springboot el modelo de Categoria
#id(int)
#nombre(String),
#fechaCreacion(LocalDate),
#responsable(String),
#justificacion(String),
#descrpcion(String),
#estado(Boolean), 
#fechaModificacion(LocalDate),
#codigo(String)
import random
from datetime import datetime, timedelta

def simular_tabla_categoria(numeroUsuarios):
    #Defino atributo base
    usuario = input()
    nombre = ["Alimentos", "Transporte", "Entretenimiento", "Educacion", "Tecnologia", "Hogar"]
    responsable = [usuario]
    justificacion = ["era necesario", "no tenia efectivo", "no tenian cambio en efectivo", "solo queria" ]
    descripcion = ["descripcion al azar", "descripcion al azar 1", "descripcion al azar 2", "descripcion al azar 3"]
    codigo = ["Z748", "F899", "T001", "G2025", "V788"]
    
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
        
            fechaInicialAnios = datetime(2025, 1, 1)
            fechaBaseAnio = fechaInicialAnios + timedelta(days=random.randint(1, 365))

            fechaModificacion = datetime(2026, 1, 1)
            fechaBaseModificacion = fechaModificacion + timedelta(days=random.randint(1, 365))


            servicio = {
                "id" : random.randint(1,1000),
                "NombreCategoria" : random.choice(nombre),
                "fechaDeCreacion" : fechaBaseAnio.strftime("%Y/%m/%d"),
                "responsable" : responsable,
                "justificacion" : random.choice(justificacion),
                "descripcion" : random.choice(descripcion),
                "estado" : random.choice(estado),
                "fechaModificacion" : fechaBaseModificacion.strftime("%Y/%m/%d"),
                "codigo" : random.choice(estado)
            }

            servicios.append(servicio)
    return servicios