import requests

def consumir_api_zend():
    url="http://localhost:8081/apizent/v1/categorias"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos=respuesta.json()
    return datos

consumir_api_zend()