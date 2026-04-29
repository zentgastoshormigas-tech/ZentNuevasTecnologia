import pandas as pd
import random

def simular_tabla_usuario(numeroUsuarios):
    #Defino atributo base
    nombres = ["Julio", "Cesar", "Joshua", "Karin", "Leo"]
    franquicia = ["MasterCard", "Visa", "American Express"]
    estado = [True, False]
  


    servicios = []
    for _ in range (numeroUsuarios):



            servicio = {
                "id" : random.randint(1,1000),
                "nombre" : random.choice(nombres),
                "franquicia" : random.choice(franquicia),
                "estado" : random.choice(estado)
            }

            #Inyectando errores controlados
            probabilidadError=random.random()
            if(probabilidadError<0.1):
                servicio["id"]=None
            elif(probabilidadError<0.2):
                servicio["nombre"]=" "+servicio["nombre"].upper()
            elif(probabilidadError<0.3):
                servicio["franquicia"]=random.choice(["dinner clubs", "hamburguesa" ])
            elif(probabilidadError<0.4):
                servicio["estado"]= None
       

            servicios.append(servicio)
            return servicios