# Se importa móduclo json
import json

datos_lectura : dict
diccionario_uno : dict
diccionario_dos : dict
claves : list
lista_deportes : list
lista_edades : list
lista_nombres : list
nombre_uno : str
nombre_dos : str
limitacion : str
deporte : str
encoding : str
contenido : str
limite_inferior : float
limite_superior : float

def seleccionar_deporte(datos_lectura : dict, claves : list) -> None:
    """
    Selecciona un deporte de una lista combinada de dos diccionarios y 
    muestra quién practica dicho deporte.

    Args:
        datos_lectura (dict): Diccionario que contiene la información de los
        deportes.
        
        claves (list): Lista de dos claves para acceder a los diccionarios
        dentro de datos_lectura.
        
    Returns:
        None: La función no retorna ningún valor, solo imprime información
        basada en el deporte seleccionado.
        
    """

    # Se accede a los diccionarios usando las claves proporcionadas
    diccionario_uno = datos_lectura[claves[0]]
    diccionario_dos = datos_lectura[claves[1]]

    # Se combinan las listas de deportes de ambos diccionarios
    lista_deportes = diccionario_uno["deportes"] + diccionario_dos["deportes"]

    # Se muestra la lista de deportes disponibles
    print(f"Deportes: {", ".join(lista_deportes)}\n")

    # Se solicita el nombre de un deporte 
    deporte = input("Ingrese el deporte a seleccioar")

    # Se determina quién practica el deporte seleccionado
    if deporte.lower() == "ajedrez" or deporte.lower() == "gimnasia":
        print("Juan Antonio Díaz Coronado y" 
            f" Dorotea Maritza Luna Sol practican {deporte}\n")

    elif deporte.lower() ==  "fútbol" or deporte.lower() == "futbol":
        print(f"Juan Antonio Díaz Coronado practica {deporte}\n")

    elif deporte.lower() == "baloncesto":
        print(f"Dorotea Maritza Luna Sol practica {deporte}\n")
    else:
        print(f"La entrada {deporte } no coincide con los deportes disponibles\n")

    return None

def rango_edad(datos_lectura : dict, claves : list) -> None:
    """
    La función determina si las edades en dos diccionarios están dentro de 
    un rango específico.
    
    Args:
        datos_lectura (dict): Diccionario que contiene información de las
        edades.
        
        claves (list): Lista de dos claves para acceder a los diccionarios
        dentro de datos_lectura.
        

    Returns:
        None: La función no retorna ningún valor, solo imprime información
        basada en el rango de edades.
    """

    # Se accede a los diccionarios usando las claves proporcionadas
    diccionario_uno = datos_lectura[claves[0]]
    diccionario_dos = datos_lectura[claves[1]]

    # Se crea y combina la lista de edades de ambos diccionarios
    lista_edades = []
    lista_edades = (lista_edades 
                    + [diccionario_uno["edad"]] 
                    + [diccionario_dos["edad"]])
    
    # Se crean los nombres completos combinando nombres y apellidos
    nombre_uno = diccionario_uno["nombres"] + " " + diccionario_uno["apellidos"]
    nombre_dos = diccionario_dos["nombres"] + " " + diccionario_dos["apellidos"]

    # Se crea y combina la lista de nombres completos
    lista_nombres = []
    lista_nombres = lista_nombres + [nombre_uno] + [ nombre_dos]

    # Se solicita el rango de edades al usuario
    limite_inferior = float(input("Ingrese el límite inferior del rango"))
    limite_superior = float(input("Ingrese el límite superior del rango"))
    limitacion = input("Escriba cerrado o abierto para limitar el intérvalo")

    # Se comprueba si el rango es cerrado
    if limitacion == "cerrado":

        # Se imprime el rango de edades
        print(f"Rango: {limite_inferior} <= {limite_superior}")

        # Se verifica si las edades están dentro del rango cerrado
        if (limite_inferior <= lista_edades[0] <= limite_superior and 
            limite_inferior <= lista_edades[1] <= limite_superior):
            
            print(f"{lista_nombres[0]} tiene {lista_edades[0]},\n"
                  f"{lista_nombres[1]} tiene {lista_edades[1]} y\n" 
                  "sus edades están en el rango ingresado")

        elif limite_inferior <= lista_edades[0] <= limite_superior:
            print(f"{lista_nombres[0]} tiene {lista_edades[0]} y\n" 
                  "su edad está en el rango ingresado")        

        elif limite_inferior <= lista_edades[1] <= limite_superior:
            print(f"{lista_nombres[1]} tiene {lista_edades[1]} y\n" 
                  "su edad está en el rango ingresado")
        else:
            print("Ninguna de las edades se encuentra en el rango ingresado")

    # Se comprueba si el rango es abierto
    elif limitacion == "abierto":

        # Se imprime el rango de edades
        print(f"Rango: {limite_inferior} < {limite_superior}")

        # Se verifica si las edades están dentro del rango abierto
        if (limite_inferior < lista_edades[0] < limite_superior and 
            limite_inferior < lista_edades[1] < limite_superior):
            
            print(f"{lista_nombres[0]} tiene {lista_edades[0]},"
                  f" {lista_nombres[1]} tiene {lista_edades[1]} y\n" 
                  "sus edades están en el rango ingresado")

        elif limite_inferior < lista_edades[0] < limite_superior:
            print(f"{lista_nombres[0]} tiene {lista_edades[0]} y" 
                  " su edad está en el rango ingresado")        

        elif limite_inferior < lista_edades[1] < limite_superior:
            print(f"{lista_nombres[1]} tiene {lista_edades[1]} y" 
                  " su edad está en el rango ingresado")
        else:
            print("Ninguna de las edades se encuentra en el rango ingresado")

    return None

if __name__ == "__main__":

    # Se abre archivo "datos.json" en modo lectura con codificación utf-8
    with open("datos.json", "r", encoding= "utf-8") as archivo:
        
        # Se lee el contenido del archivo
        contenido = archivo.read()  
    
    # Se carga el contenido JSON en un diccionario de datos
    datos_lectura = json.loads(contenido) 

    # Se extraen las claves del diccionario y las convierte en una lista
    claves = datos_lectura.keys()    
    claves = list(claves)

    # Se Llama a función seleccionar_deporte con datos leídos y claves
    seleccionar_deporte(datos_lectura, claves)

    # Se llama a la función rango_edad con los datos leídos y las claves
    rango_edad(datos_lectura, claves)