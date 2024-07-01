import requests
import json

respuesta : requests.models.Response
cosas : dict
url : str
nombre : str

def mostrar_uno(url : str) -> None:
    """
    Muestra pares clave-valor de una API que proporciona datos aleatorios 
    sobre gatos.
    
    Args:
        url (str): La URL de la API para obtener datos aleatorios sobre gatos.

    Returns:
        None
    """

    # Se realiza una solicitud GET a la API
    respuesta = requests.get(url)

    # Se convierte la respuesta de la API de JSON a un diccionario
    cosas = json.loads(respuesta.content)

    # Se imprimen los pares clave-valor
    print("\033[4mPares llave :"
          " valor de API que arroja datos random sobre gatos\033[0m")
    for k, v in cosas.items():
        if k != "length":
            print(f"Clave: {k} | Valor: {v}\n")
        else:
            print(f"Clave: {k} | Valor: {v}\n"
                  "* lengt: Longitud del mensaje en el valor de la clave 'fact'\n") 
            
    return respuesta, cosas

def mostrar_dos(url : str, respuesta : requests.models.Response, 
                cosas : dict) -> None:

    # Se realiza una solicitud GET a la API
    respuesta = requests.get(url)

    # Se convierte la respuesta de la API de JSON a un diccionario
    cosas = json.loads(respuesta.content)

    # Se imprimen los pares clave-valor
    print("\033[4mPares llave : valor de API que arroja chistes random\033[0m")
    for k, v in cosas.items():
        if k != "id":
            print(f"Clave: {k} | Valor: {v}\n")
        else:
            print(f"Clave: {k} | Valor: {v}\n"
                  "* id: Código del chiste\n")

    return respuesta, cosas

def mostrar_tres(url : str, respuesta : requests.models.Response, 
                 cosas : dict) -> None:

    # Se realiza una solicitud GET a la API
    respuesta = requests.get(url)

    # Se convierte la respuesta de la API de JSON a un diccionario
    cosas = json.loads(respuesta.content)

    # Se imprimen los pares clave-valor
    print("\033[4mPares llave :"
          " valor de API que arroja links de imágenes de perros random\033[0m")
    for k, v in cosas.items():
        if k != "message":
            print(f"Clave: {k} | Valor: {v}\n")
        else:
            print(f"Clave: {k} | Valor: {v}\n"
                  "* message: link de la imagen random del perro\n")

    return respuesta, cosas

def mostrar_cuatro(url : str, respuesta : requests.models.Response, 
                   cosas : dict) -> None:

    # Se realiza una solicitud GET a la API
    respuesta = requests.get(url)

    # Se convierte la respuesta de la API de JSON a un diccionario
    cosas = json.loads(respuesta.content)

    # Se imprimen los pares clave-valor
    print("\033[4mPares llave :"
          " valor de API que arroja información sobre un usuario falso random\033[0m")
    for k, v in cosas.items():
        if k != "info":
            print(f"Clave: {k} | Valor: {v}\n")
        else:
            print(f"Clave: {k} | Valor: {v}\n"
                  "* info: Información meta sobre la solicitud de datos\n")

    return respuesta, cosas

def mostrar_cinco(url : str, nombre : str, respuesta : requests.models.Response, 
                  cosas : dict) -> None:

    # Se realiza una solicitud GET a la API
    respuesta = requests.get(url)

    # Se convierte la respuesta de la API de JSON a un diccionario
    cosas = json.loads(respuesta.content)

    # Se imprimen los pares clave-valor
    print("\033[4mPares llave : valor de API que predice la "
          "nationalidad de una persona basadoa en su nombre\033[0m")
    for k, v in cosas.items():
        if k != "count":
            print(f"Clave: {k} | Valor: {v}\n")
        else:
            print(f"Clave: {k} | Valor: {v}\n"
                  f"* count: cantidad total de datos o nombres similares a "
                  f"{nombre.title()} en la base de datos de la API\n")
            
    return None

if __name__ == "__main__":
    # Se define la URL
    url = "https://catfact.ninja/fact"

    # Se llama a la función para mostrar pares clave-valor de la API
    respuesta, cosas = mostrar_uno(url)

    # Se define la URL
    url = "https://official-joke-api.appspot.com/random_joke"

    # Se llama a la función para mostrar pares clave-valor de la API
    respuesta, cosas = mostrar_dos(url, respuesta, cosas)

    # Se define la URL
    url = "https://dog.ceo/api/breeds/image/random"
    
    # Se llama a la función para mostrar pares clave-valor de la API
    respuesta, cosas = mostrar_tres(url, respuesta, cosas)

    # Se define la URL
    url = "https://randomuser.me/api/"

    # Se llama a la función para mostrar pares clave-valor de la API
    respuesta, cosas = mostrar_cuatro(url, respuesta, cosas)

    # Se solicita al usuario que ingrese un nombre
    nombre = input("Ingrese el nombre de una persona")
    
    # Se define la URL
    url = (f"https://api.nationalize.io?name={nombre.title()}")

    # Se llama a la función para mostrar pares clave-valor de la API
    mostrar_cinco(url, nombre, respuesta, cosas)