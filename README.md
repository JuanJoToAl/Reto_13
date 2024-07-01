# Reto_13
El siguiente repositorio contiene las propuestas de soluciones a los puntos del reto 13
## 1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

```python
lista_claves : list
valores : list
valores_ordenados : list
lista_claves_uno : list
tipo : str
clave : str
valor : str
bandera : bool
diccionario : dict

def llenar_claves(lista_claves : list) -> tuple:
    """
    La función permite al usuario ingresar claves de tipo entero, flotante,
    cadena de texto o tupla. El proceso se repite hasta que el usuario 
    ingresa 'fin' como clave cuando se especifica el tipo de dato 'str'.
    

    Args:
        lista_claves (list): Una lista donde se almacenarán las claves
        ingresadas por el usuario.
        

    Returns:
        tuple: Una tupla que contiene tres elementos:
            - lista_claves (list): La lista actualizada con las claves
              ingresadas por el usuario.

            - bandera (bool): Un valor booleano que indica si el proceso de
              ingreso de claves debe continuar.

            - clave (int, float, str, tuple): La última clave ingresada por el
              usuario, con el tipo de dato correspondiente.
            
    """
    
    # Variable para controlar el ciclo de entrada de datos
    bandera = True

    # Se solicita al usuario el tipo de dato para la clave
    tipo = input("Tipo de dato para la clave:")

    # Se solicita al usuario una clave
    clave = input("Ingrese una clave (o 'fin' para terminar): ")

    # Se procesa según el tipo de dato especificado
    if tipo.lower() == "int":
        try:
            # Se intenta convertir la clave a un entero y añadirla a la lista
            clave = int(clave)
            lista_claves.append(clave)
        except ValueError:

            # Se imprime el mensaje de error si la conversión falla
            print(f"Error: '{clave}' no es válido para tipo int.")

    # Se procesa según el tipo de dato especificado
    elif tipo.lower() == "float":
        try:
            # Se intenta convertir la clave a un flotante y añadirla a la lista
            clave = float(clave)
            lista_claves.append(clave)
        except ValueError:

            # Se imprime el mensaje de error si la conversión falla
            print(f"Error: '{clave}' no es válido para tipo float.")

    # Se terminar el ciclo si el tipo de dato es str y la clave es 'fin'
    elif tipo.lower() == "str" and clave.lower() == "fin":
        bandera = False

    # Se procesa según el tipo de dato especificado
    elif tipo.lower() == "str":

        # Se añade la clave a la lista si el tipo de dato es str
        lista_claves.append(clave)
    
    # Se procesa según el tipo de dato especificado
    elif tipo.lower() == "tuple":

        # Se convierte la clave a una tupla y se añade a la lista
        clave = clave.split(",")
        clave = tuple(clave)
        lista_claves.append(clave)

    # Se imprime el mensaje de error si el tipo de dato no es válido
    elif tipo != "str" or "int" or "flaot" or "tuple":
        print(f"Error: '{tipo}' no es un tipo de dato válido\n")

    return lista_claves, bandera, clave, tipo

def llenar_valores(diccionario : dict, clave : str, tipo : str) -> dict:
    """
    La función solicita al usuario el tipo de dato y el valor para la clave
    proporcionada. Los datos pueden ser de tipo entero, flotante, cadena de
    texto, tupla o lista.
    
    Args:
        diccionario (dict): El diccionario al que se añadirá el valor para la
        clave especificada.

        clave (str): La clave en el diccionario para la que se establecerá un
        nuevo valor.
        
    Returns:
        diccionario (dict): Diccionario actualizado con el nuevo valor asociado
        a la clave.
    """

    # Se solicita al usuario el tipo de dato para el valor de la clave
    tipo = input(f"Tipo de dato para el valor de la clave '{clave}':")

    # Se solicita al usuario el valor para la clave
    valor = input(f"Valor para la clave '{clave}': ")

    # Se procesa el tipo de dato especificado por el usuario
    if tipo.lower() == "int":
        try:
            # Se intenta convertir el valor a un entero y se añade al diccionario
            valor = int(valor)
            diccionario[clave] = valor
        except ValueError:

            # Se imprime un mensaje de error si la conversión falla
            print(f"Error: '{valor}' no es válido para tipo int.")
    
    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "float":
        try:

            # Se intenta convertir el valor a un flotante y se añade al diccionario
            valor = float(valor)
            diccionario[clave] = valor
        except ValueError:

            # Se imprime un mensaje de error si la conversión falla
            print(f"Error: '{valor}' no es válido para tipo float.")

    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "str":

        # Se añade el valor al diccionario si el tipo de dato es str
        diccionario[clave] = valor
    
    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "tuple":

        # Se convierte el valor a una tupla y se añade al diccionario
        valor = valor.split(",")
        valor = tuple(valor)
        diccionario[clave] = valor
    
    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "list":

        # Se convierte el valor a una lista y se añade al diccionario
        valor = valor.split(",")
        valor = list(valor)
        diccionario[clave] = valor

    # Se imprime un mensaje de error si el tipo de dato no es válido
    elif tipo != "str" or tipo != "int" or tipo != "flaot" or tipo != "tuple":
        print(f"Error: '{tipo}' no es un tipo de dato válido\n")

    return diccionario

def ordenar_valores(diccionario):
    """
    La función realiza diferentes acciones dependiendo del tipo de dato de los
    valores en el diccionario. Si todos los valores son del mismo tipo, los
    imprime en orden ascendente. Para cadenas de texto, se ordenan primero los
    números y luego las letras. Los valores de tipo tupla o lista se imprimen en 
    el orden en que fueron ingresados.

    Args:
        diccionario (dict): El diccionario cuyos valores se van a ordenar y
        mostrar.
        
    Returns:
        None: La función no retorna algún valor, solo imprime los valores
        ordenados o mensajes de error.
        
    """

    # Se obtiene la lista de valores del diccionario
    valores = list(diccionario.values())
    
    # Se verifica si el diccionario solo tiene un valor
    if len(valores) == 1:
        print("El diccionario solo tiene un valor,\n" 
              "no se puede imprimir de forma ascendente")
    
    # Se verifica si los tipos de datos de los valores son diferentes
    elif type(valores[0]) != type(valores[1]):
        print("El tipo de dato de los valores es diferente.\n" 
              "No se pueden imprimir de manera ascendente")

    # Se verifica si todos los valores son cadenas de texto (str)    
    elif type(valores[0]) == type(valores[1]) == str: 

        print("Para datos tipo str, se imprimen primero números y luego letras")
        
        # Se vuelve a obtener los valores del diccionario
        valores = list(diccionario.values())

        # Se ordenan los valores en orden ascendente
        valores_ordenados = sorted(valores)

        # Se imprimen los valores ordenados
        for valor in valores_ordenados:
            print(valor)   
    
    # Se verifica si todos los valores son tuplas (tuple)
    elif type(valores[0]) == type(valores[1]) == tuple: 

        print("Los datos tipo tuple se imprimen según el orden de\n"
              "ingreso del usuario")
        
        # Se vuelve a obtener los valores del diccionario
        valores = list(diccionario.values())

        # Se ordenan los valores en forma ascendente
        valores_ordenados = sorted(valores)

        # Se imprimen los valores ordenados
        for valor in valores_ordenados:
            print(valor)   
    
    # Se verifica si todos los valores son listas (list)
    elif type(valores[0]) == type(valores[1]) == list: 

        print("Los datos tipo list se imprimen según el orden\n" 
              "de ingreso del usuario")
        
        # Se vuelve a obtener los valores del diccionario
        valores = list(diccionario.values())

        # Se ordenan los valores en forma ascendente
        valores_ordenados = sorted(valores)

        # Se imprimen los valores ordenados
        for valor in valores_ordenados:
            print(valor)   
    
    # Se verifica si valores son del mismo tipo pero no de casos anteriores
    elif type(valores[0]) == type(valores[1]):

        # Se ordenan los valores en forma ascendente
        valores = list(diccionario.values())
        valores_ordenados = sorted(valores)

        # Se imprimen los valores ordenados
        for valor in valores_ordenados:
            print(valor)
    
    return None

if __name__ == "__main__":

    # Se inicializan lista de claves y bandera de control
    lista_claves_uno = []
    bandera = True

    # Se imprime mensaje de control para crear las claves del diccionario
    print("Diccionario uno")
    print("Elija el tipo de dato para clave:\nint, float, str o tuple.\n*" 
          " Si el dato es tuple use la coma ',' como separador\n")
    print("Para terminar ciclo: tipo = str y clave = fin\n")
    
    # Ciclo para llenar la lista de claves
    while bandera:
        lista_claves_uno, bandera, clave, tipo = llenar_claves(lista_claves_uno)
        
        # Se verifica si la clave no es "fin" y si ya existe en la lista
        if (clave != "fin" and lista_claves_uno.count(clave) != 1 and 
            clave in lista_claves_uno):

            # Se elimina la clave repetida y se muestra el mensaje
            lista_claves_uno.remove(clave)            
            print(f"La clave '{clave}' ya está en el diccionario, por lo que\n" 
                  "la primera aparición de esta no se añadirá")
            print(f"Lista de claves uno sin clave repetida {lista_claves_uno}\n")

    # Se imprime mensaje de control para crear los valores del diccionario
    print("Elija el tipo de dato para valor:\nint, float, str, list o tuple.\n*" 
          " Si el dato es tuple use la coma ',' como separador\n")

    # Se inicializa el diccionario
    diccionario = {}

    # Se llena el diccionario con los valores ingresados por el usuario
    for clave in lista_claves_uno:
        diccionario = llenar_valores(diccionario, clave, tipo)

    # Se verifica si el diccionario tiene elementos
    if diccionario:

        # Se muestra el diccionario lleno
        print("Diccionario llenado por el usuario:")
        print(f"{diccionario}\n")
        
        # Se ordena y mostra los valores del diccionario
        ordenar_valores(diccionario)
    
    else:
        # Se muestra mensaje si el diccionario está vacío
        print("El diccionario está vacío")
        print(f"{diccionario}\n")
```

## 2. Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

### Para el código se deben hacer las siguiente aclaraciones: 

* Las claves del diccionarios no pueden ser listas ni diccionarios. Esto porque los mencionados son tipos de
datos iterables

* Las tuplas en el código solo pueden tener elementos tipo str dentro de ellas

```python
lista_claves : list
valores : list
valores_ordenados : list
lista_claves_uno : list
lista_claves_dos : list
tipo : str
clave : str
valor : str
diccionario : dict
diccionario_uno : dict
diccionario_dos : dict
bandera : bool

def llenar_claves(lista_claves : list) -> tuple:
    """
    La función permite al usuario ingresar claves de tipo entero, flotante,
    cadena de texto o tupla. El proceso se repite hasta que el usuario 
    ingresa 'fin' como clave cuando se especifica el tipo de dato 'str'.
    

    Args:
        lista_claves (list): Una lista donde se almacenarán las claves
        ingresadas por el usuario.
        

    Returns:
        tuple: Una tupla que contiene tres elementos:
            - lista_claves (list): La lista actualizada con las claves
              ingresadas por el usuario.

            - bandera (bool): Un valor booleano que indica si el proceso de
              ingreso de claves debe continuar.

            - clave (int, float, str, tuple): La última clave ingresada por el
              usuario, con el tipo de dato correspondiente.
            
    """
    
    # Variable para controlar el ciclo de entrada de datos
    bandera = True

    # Se solicita al usuario el tipo de dato para la clave
    tipo = input("Tipo de dato para la clave:")

    # Se solicita al usuario una clave
    clave = input("Ingrese una clave (o 'fin' para terminar): ")

    # Se procesa según el tipo de dato especificado
    if tipo.lower() == "int":
        try:
            # Se intenta convertir la clave a un entero y añadirla a la lista
            clave = int(clave)
            lista_claves.append(clave)
        except ValueError:

            # Se imprime el mensaje de error si la conversión falla
            print(f"Error: '{clave}' no es válido para tipo int.")

    # Se procesa según el tipo de dato especificado
    elif tipo.lower() == "float":
        try:
            # Se intenta convertir la clave a un flotante y añadirla a la lista
            clave = float(clave)
            lista_claves.append(clave)
        except ValueError:

            # Se imprime el mensaje de error si la conversión falla
            print(f"Error: '{clave}' no es válido para tipo float.")

    # Se terminar el ciclo si el tipo de dato es str y la clave es 'fin'
    elif tipo.lower() == "str" and clave.lower() == "fin":
        bandera = False

    # Se procesa según el tipo de dato especificado
    elif tipo.lower() == "str":

        # Se añade la clave a la lista si el tipo de dato es str
        lista_claves.append(clave)
    
    # Se procesa según el tipo de dato especificado
    elif tipo.lower() == "tuple":

        # Se convierte la clave a una tupla y se añade a la lista
        clave = clave.split(",")
        clave = tuple(clave)
        lista_claves.append(clave)

    # Se imprime el mensaje de error si el tipo de dato no es válido
    elif tipo != "str" or "int" or "flaot" or "tuple":
        print(f"Error: '{tipo}' no es un tipo de dato válido\n")

    return lista_claves, bandera, clave, tipo

def llenar_valores(diccionario : dict, clave : str, tipo : str) -> dict:
    """
    La función solicita al usuario el tipo de dato y el valor para la clave
    proporcionada. Los datos pueden ser de tipo entero, flotante, cadena de
    texto, tupla o lista.
    
    Args:
        diccionario (dict): El diccionario al que se añadirá el valor para la
        clave especificada.

        clave (str): La clave en el diccionario para la que se establecerá un
        nuevo valor.
        
    Returns:
        diccionario (dict): Diccionario actualizado con el nuevo valor asociado
        a la clave.
    """

    # Se solicita al usuario el tipo de dato para el valor de la clave
    tipo = input(f"Tipo de dato para el valor de la clave '{clave}':")

    # Se solicita al usuario el valor para la clave
    valor = input(f"Valor para la clave '{clave}': ")

    # Se procesa el tipo de dato especificado por el usuario
    if tipo.lower() == "int":
        try:
            # Se intenta convertir el valor a un entero y se añade al diccionario
            valor = int(valor)
            diccionario[clave] = valor
        except ValueError:

            # Se imprime un mensaje de error si la conversión falla
            print(f"Error: '{valor}' no es válido para tipo int.")
    
    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "float":
        try:

            # Se intenta convertir el valor a un flotante y se añade al diccionario
            valor = float(valor)
            diccionario[clave] = valor
        except ValueError:

            # Se imprime un mensaje de error si la conversión falla
            print(f"Error: '{valor}' no es válido para tipo float.")

    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "str":

        # Se añade el valor al diccionario si el tipo de dato es str
        diccionario[clave] = valor
    
    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "tuple":

        # Se convierte el valor a una tupla y se añade al diccionario
        valor = valor.split(",")
        valor = tuple(valor)
        diccionario[clave] = valor
    
    # Se procesa el tipo de dato especificado por el usuario
    elif tipo.lower() == "list":

        # Se convierte el valor a una lista y se añade al diccionario
        valor = valor.split(",")
        valor = list(valor)
        diccionario[clave] = valor

    # Se imprime un mensaje de error si el tipo de dato no es válido
    elif tipo != "str" or tipo != "int" or tipo != "flaot" or tipo != "tuple":
        print(f"Error: '{tipo}' no es un tipo de dato válido\n")

    return diccionario

def combinar_dicts(diccionario_uno : dict, diccionario_dos : dict) -> list:
    """
    Esta función toma dos diccionarios como entrada y actualiza el primer
    diccionario con los elementos del segundo diccionario. Si hay claves
    duplicadas, los valores del segundo diccionario sobrescribirán los 
    valores del primer diccionario.
    

    Args:
        diccionario_uno (dict): El primer diccionario que será actualizado.
        
        diccionario_dos (dict): El segundo diccionario cuyos elementos se
        agregarán al primero.
        
    Returns:
        diccionario_uno (dict): El primer diccionario actualizado con los
        elementos del segundo diccionario.
    """

    # Se actualiza el primer diccionario con los elementos del segundo
    diccionario_uno.update(diccionario_dos)

    # Se devuelve el diccionario combinado
    return diccionario_uno

if __name__ == "__main__":

    # Se inicializa lista de claves y bandera de control, diccionario uno
    lista_claves_uno = []
    bandera = True

    # Se imprime mensaje de control para crear las claves del diccionario
    print("Diccionario uno")
    print("Elija el tipo de dato para clave:\nint, float, str o tuple.\n*" 
          " Si el dato es tuple use la coma ',' como separador\n")
    print("Para terminar ciclo: tipo = str y clave = fin\n")
    
    # Ciclo para llenar la lista de claves del primer diccionario
    while bandera:
        lista_claves_uno, bandera, clave, tipo = llenar_claves(lista_claves_uno)
        
        # Se verifica si la clave no es "fin" y si ya existe en la lista
        if (clave != "fin" and lista_claves_uno.count(clave) != 1 and 
            clave in lista_claves_uno):

            # Se elimina la clave repetida y se muestra el mensaje
            lista_claves_uno.remove(clave)            
            print(f"La clave '{clave}' ya está en el diccionario, por lo que\n" 
                  "la primera aparición de esta no se añadirá")
            print(f"Lista de claves uno sin clave repetida {lista_claves_uno}")

    # Se imprime mensaje de control para crear las claves del diccionario
    print("Elija el tipo de dato para valor:\nint, float, str, list o tuple.\n*" 
          " Si el dato es tuple use la coma ',' como separador\n")

    # Se inicializa el primer diccionario
    diccionario_uno = {}

    # Se llenar el diccionario uno con valores ingresados por el usuario
    for clave in lista_claves_uno:
        diccionario_uno = llenar_valores(diccionario_uno, clave, tipo)

    # Se verifica si el primer diccionario tiene elementos
    if diccionario_uno:

        # Se muestra el primer diccionario lleno
        print("Diccionario uno llenado por el usuario:")
        print(f"{diccionario_uno}\n")

    else:
        # Se muestra el mensaje si el primer diccionario está vacío
        print("El diccionario uno está vacío")
        print(f"{diccionario_uno}\n")

    # Se inicializa lista de claves y bandera de control, diccionario dos
    lista_claves_dos = []
    bandera = True
    
    # Se imprime mensaje de control para crear las claves del diccionario
    print("Diccionario dos")
    print("Elija el tipo de dato para clave:\nint, float, str o tuple.\n*" 
          " Si el dato es tuple use la coma ',' como separador\n")
    print("Para terminar ciclo: tipo = str y clave = fin\n")

    # Ciclo para llenar la lista de claves del segundo diccionario
    while bandera:
        lista_claves_dos, bandera, clave, tipo = llenar_claves(lista_claves_dos)
        
        # Se verifica si la clave no es "fin" y si ya existe en la lista
        if (clave != "fin" and lista_claves_dos.count(clave) != 1 
            and clave in lista_claves_dos):
            
            # Se elimina la clave repetida y se muestra el mensaje
            lista_claves_dos.remove(clave)            
            print(f"La clave '{clave}' ya está en el diccionario, por lo que\n" 
                  "la primera aparición de esta no se añadirá")
            print(f"Lista de claves dos sin clave repetida {lista_claves_dos}")

    # Se imprime mensaje de control para crear las claves del diccionario
    print("Elija el tipo de dato para valor:\nint, float, str, list o tuple.\n*" 
          " Si el dato es tuple use la coma ',' como separador\n")

    # Se inicializa el segundo diccionario
    diccionario_dos = {}
    
    # Se llenar el diccionario dos con valores ingresados por el usuario
    for clave in lista_claves_dos:
        diccionario_dos = llenar_valores(diccionario_dos, clave, tipo)

    # Se verifica si el segundo diccionario tiene elementos
    if diccionario_dos:

        # Se muestra el segundo diccionario lleno
        print("Diccionario dos llenado por el usuario:")
        print(f"{diccionario_dos}\n")

    else:
        # Se muestra mensaje si el segundo diccionario está vacío
        print("El diccionario dos está vacío")
        print(f"{diccionario_dos}\n")
    
    # Se combinan los dos diccionarios
    diccionario_uno = combinar_dicts(diccionario_uno, diccionario_dos)

    # Se muestra el diccionario combinado
    print(f"Diccionario uno y dos combinados:\n{diccionario_uno}")
```
## 3. Dado el JSON:
```JSON
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Daz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
 Cree un programa que lea de un archivo con dicho JSON y: 
 - Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
 - Imprima los nombres completos (nombre y apellidos) de las personas que estén
   en un rango de edades dado por el usuario.
 
```python
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
```

## 4. El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:

```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```

Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' ([aquí](https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date) pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.

### Para el código se debe hacer la siguiente acalración:
* Se ha creado un archivo o módulo para descargar llamado clima, del cual se importa la variable jsonString. Lo anterior para no colocar un str tan largo en el código.
```python
# Se importa módulo json
import json

# Obtiene módulo para obtener fecha y hora en UTC
from datetime import datetime, timezone

# Se importa la variable con los datos de la predicción del clima
from clima import jsonString

data : dict
jsonString : str
evento : str
lista_alerta : list
lista_precipitacion : list
lista_tpm_max : list
lista_tpm_min : list
lista_vel_viento : list
indice_alerta : list
indice_precipitacion : list
indice_tpm_min : list
indice_vel_viento : list
indice_tpm_max : list
fecha_alerta : list
fecha_precipitacion : list
fecha_tpm_min : list
fecha_vel_viento : list
fecha_tpm_max : list
fecha_evento : list
descripcion_evento : list
presion : list
humedad : list
nubosidad : list
precipitacion : list
punto_rocio : list
uvi : list
temp_dia : list
tmp_min : list
tmp_max : list
tmp_noche : list
tmp_tarde : list
tmp_mañana : list
ssc_term_dia : list
ssc_term_noche : list
ssc_term_tarde : list
ssc_term_mañana : list
vel_viento : list
dir_viento : list
rafaga_viento : list

def indice(lista_evento : list) -> list:
    """
    Genera una lista con los índices de las ocurrencias del elemento 'X' en 
    la lista proporcionada.
    

    Args:
        lista_evento (list): Una lista de elementos donde se buscarán las
        ocurrencias de 'X'.
        
    Returns:
        list (list): Una lista de índices donde 'X' aparece en la lista
        proporcionada.
    """

    # Se inicializa una lista vacía para almacenar los índices
    lista_indice = []

    for x in lista_evento:
        if x == "X":

            # Se añade el índice de 'X' en lista_evento a lista_indice
            lista_indice.append(lista_evento.index(x))

    return lista_indice

def fecha(indice_evento : list, data : dict) -> list:
    """
    Obtiene las fechas de eventos basadas en una lista de índices y un
    diccionario de datos.

    Args:
        indice_evento (list): Una lista de índices que indican las posiciones
        de los eventos.
        
        data (dict): Contiene las fechas de los eventos en
        el formato {"dt": {indice: fecha}}.

    Returns:
        list (list): Lista de fechas correspondientes a los índices
        proporcionados.
    """

    # Se inicializa lista vacía para almacenar las fechas de los eventos
    fecha_evento = []
    
    for x in indice_evento:
        # Se convierte el índice a cadena de texto
        x = str(x)
        
        # Se añade la fecha correspondiente al índice en fecha_evento
        fecha_evento.append(data["dt"][x])

    return fecha_evento

def factor_evento(indice_evento : list, data : dict, evento : str) -> tuple:
    """
    Procesa y devuelve información específica de un evento basado en los
    índices proporcionados y el tipo de evento.
    
    Args:
        indice_evento (list): Lista de índices de eventos.

        data (dict): Diccionario que contiene los datos de los eventos.

        evento (str): Tipo de evento a procesar ("alerta", "precipitacion",
        "tpm_max", "tpm_min", "vel_viento").
        
    Returns:
        tuple: lista de fechas si el evento es "alerta", o una tupla de
        listas con datos específicos del evento para otros tipos.
    """

    if evento == "alerta":

        # Se inicializa lista para almacenar las fechas de los eventos de alerta
        fecha_evento = []
        for x in indice_evento:

            # Se convierte el índice a cadena de texto
            x = str(x)

            # Se añade la fecha correspondiente al índice en fecha_evento
            fecha_evento.append(data["dt"][x])

        # Se retorna la lista de fechas de alerta
        return fecha_evento
    
    elif evento == "precipitacion":
        # Se inicializan listas para almacenar datos del evento de precipitación
        descripcion_evento = []
        for x in indice_evento:
            x = str(x)
            descripcion_evento.append(data["description"][x])

        presion = []
        for x in indice_evento:
            x = str(x)
            presion.append(data["pressure"][x])

        humedad = []
        for x in indice_evento:
            x = str(x)
            humedad.append(data["humidity"][x])

        nubosidad = []
        for x in indice_evento:
            x = str(x)
            nubosidad.append(data["clouds"][x])

        precipitacion = []
        for x in indice_evento:
            x = str(x)
            precipitacion.append(data["prcp"][x])
        
        punto_rocio = []
        for x in indice_evento:
            x = str(x)
            punto_rocio.append(data["dew_point"][x])
            
        return (descripcion_evento, presion, 
                humedad, nubosidad, 
                precipitacion, punto_rocio)
    
    elif evento == "tpm_max":
        # Se inicializan listas y almacenan datos del evento temperatura máxima
        humedad = []
        for x in indice_evento:
            x = str(x)
            humedad.append(data["humidity"][x])

        uvi = []
        for x in indice_evento:
            x = str(x)
            uvi.append(data["uvi"][x])
        
        temp_dia = []
        for x in indice_evento:
            x = str(x)
            temp_dia.append(data["temp.day"][x])
        
        tmp_min = []
        for x in indice_evento:
            x = str(x)
            tmp_min.append(data["tmpMin"][x])
        
        tmp_max = []
        for x in indice_evento:
            x = str(x)
            tmp_max.append(data["tmpMax"][x])

        tmp_noche = []
        for x in indice_evento:
            x = str(x)
            tmp_noche.append(data["temp.night"][x])

        tmp_tarde = []
        for x in indice_evento:
            x = str(x)
            tmp_tarde.append(data["temp.eve"][x])
        
        tmp_mañana = []
        for x in indice_evento:
            x = str(x)
            tmp_mañana.append(data["temp.morn"][x])       

        ssc_term_dia = []
        for x in indice_evento:
            x = str(x)
            ssc_term_dia.append(data["feels_like.day"][x])  
        
        ssc_term_noche = []
        for x in indice_evento:
            x = str(x)
            ssc_term_noche.append(data["feels_like.night"][x])

        ssc_term_tarde = []
        for x in indice_evento:
            x = str(x)
            ssc_term_tarde.append(data["feels_like.eve"][x])     

        ssc_term_mañana = []
        for x in indice_evento:
            x = str(x)
            ssc_term_mañana.append(data["feels_like.morn"][x])

        return (humedad, uvi, temp_dia, 
                tmp_min, tmp_max, tmp_mañana,
                tmp_tarde, tmp_noche, ssc_term_dia, 
                ssc_term_mañana, ssc_term_tarde, ssc_term_noche)

    elif evento == "tpm_min":
        # Se inicializan listas y almacenan datos del evento temperatura mínima
        humedad = []
        for x in indice_evento:
            x = str(x)
            humedad.append(data["humidity"][x])

        uvi = []
        for x in indice_evento:
            x = str(x)
            uvi.append(data["uvi"][x])
        
        temp_dia = []
        for x in indice_evento:
            x = str(x)
            temp_dia.append(data["temp.day"][x])
        
        tmp_min = []
        for x in indice_evento:
            x = str(x)
            tmp_min.append(data["tmpMin"][x])
        
        tmp_max = []
        for x in indice_evento:
            x = str(x)
            tmp_max.append(data["tmpMax"][x])

        tmp_noche = []
        for x in indice_evento:
            x = str(x)
            tmp_noche.append(data["temp.night"][x])

        tmp_tarde = []
        for x in indice_evento:
            x = str(x)
            tmp_tarde.append(data["temp.eve"][x])
        
        tmp_mañana = []
        for x in indice_evento:
            x = str(x)
            tmp_mañana.append(data["temp.morn"][x])       

        ssc_term_dia = []
        for x in indice_evento:
            x = str(x)
            ssc_term_dia.append(data["feels_like.day"][x])  
        
        ssc_term_noche = []
        for x in indice_evento:
            x = str(x)
            ssc_term_noche.append(data["feels_like.night"][x])

        ssc_term_tarde = []
        for x in indice_evento:
            x = str(x)
            ssc_term_tarde.append(data["feels_like.eve"][x])     

        ssc_term_mañana = []
        for x in indice_evento:
            x = str(x)
            ssc_term_mañana.append(data["feels_like.morn"][x])

        return (humedad, uvi, temp_dia, 
                tmp_min, tmp_max, tmp_mañana,
                tmp_tarde, tmp_noche, ssc_term_dia, 
                ssc_term_mañana, ssc_term_tarde, ssc_term_noche)

    elif evento == "vel_viento":
        # Se inicializan listas y almacenan datos, evento: velocidad del viento
        descripcion_evento = []
        for x in indice_evento:
            x = str(x)
            descripcion_evento.append(data["description"][x])

        presion = []
        for x in indice_evento:
            x = str(x)
            presion.append(data["pressure"][x])

        nubosidad = []
        for x in indice_evento:
            x = str(x)
            nubosidad.append(data["clouds"][x])

        vel_viento = []
        for x in indice_evento:
            x = str(x)
            vel_viento.append(data["velViento"][x])
        
        dir_viento = []
        for x in indice_evento:
            x = str(x)
            dir_viento.append(data["dirViento"][x])
        
        rafaga_viento = []
        for x in indice_evento:
            x = str(x)
            rafaga_viento.append(data["wind_gust"][x])



        return (descripcion_evento, presion, 
                nubosidad, vel_viento, 
                dir_viento, rafaga_viento)
    
if __name__ == "__main__":
    # Se carga el contenido del archivo JSON en la variable data
    data = json.loads(jsonString)

    # Se convierten los valores de las claves en listas
    lista_alerta = list(data['alertAlertas'].values())
    lista_precipitacion = list(data['alertPrecip'].values())
    lista_tpm_max = list(data['alertTmpMax'].values())
    lista_tpm_min = list(data['alertTmpMin'].values())
    lista_vel_viento = list(data['alertVelViento'].values())

    #  Se procesan las alertas de alertAlertas
    if "X" in lista_alerta:
        # Se obtienen los índices de la lista de alertAlertas
        indice_alerta = indice(lista_alerta)

        # Se obtienen las fechas del evento usando los/el índice/s obtenido/s
        fecha_alerta = fecha(indice_alerta, data)

        # Se formatean las fechas de la precipitación
        for x in range(len(fecha_alerta)):
            fecha_alerta.append(datetime.fromtimestamp
                                       (fecha_alerta[x], timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
            fecha_alerta.pop(0)

        # Se establece el evento como "alerta"
        evento = "alerta"
        
        # Se obtienen los datos del evento de alertAlertas
        fecha_evento = factor_evento(indice_alerta, data, evento)

        # Se imprimen los datos del evento de alertAlertas
        for x in range(len(fecha_alerta)):
            print(f"* En la fecha {fecha_alerta[x]} se pronostica" 
                  " una alerta de alertAlertas")

    # Se procesan las alertas de la precipitación
    if "X" in lista_precipitacion:

        # Se obtienen los índices de la lista de precipitaciones
        indice_precipitacion = indice(lista_precipitacion)

        # Se obtienen las fechas del evento usando los/el índice/s obtenido/s
        fecha_precipitacion = fecha(indice_precipitacion, data)

        # Se formatean las fechas de la precipitación
        for x in range(len(fecha_precipitacion)):
            fecha_precipitacion.append(datetime.fromtimestamp
                                       (fecha_precipitacion[x], timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
            fecha_precipitacion.pop(0)

        # Se establece el evento como "precipitacion"
        evento = "precipitacion"
        
        # Se obtienen los datos del evento de la precipitación
        (descripcion_evento, presion, 
         humedad, nubosidad, 
         precipitacion, punto_rocio) = factor_evento(indice_precipitacion, data, evento)
        
        # Se imprimen los datos del evento de precipitación
        for x in range(len(fecha_precipitacion)):
            print(f"* En la fecha {fecha_precipitacion[x]} se pronostica" 
                  " una alerta de precipitación")
            print("Los datos del evento son:\n")
            print(f"Descripción del estado del tiempo: {descripcion_evento[x]}"
                  f" | Presión atmosférica: {presion[x]} hPa")
            print(f"Humedad relativa: {humedad[x]}%"         
                  f" | Porcentaje de nubosidad: {nubosidad[x]}%")
            print(f"Precipitación: {precipitacion[x]} mm"
                  f" | Punto de rocío: {punto_rocio[x]}°C\n")

    # Se procesan las alertas de la temperatura mínima
    if "X" in lista_tpm_min:

        # Se obtienen los índices de la lista de temperatura mínima
        indice_tpm_min = indice(lista_tpm_min)

        # Se obtienen las fechas del evento usando los/el índice/s obtenido/s
        fecha_tpm_min = fecha(indice_tpm_min, data)

        # Se formatean las fechas de la temperatura mínima
        for x in range(len(fecha_tpm_min)):
            fecha_tpm_min.append(datetime.fromtimestamp
                                 (fecha_tpm_min[x], timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
            fecha_tpm_min.pop(0)

        # Se establece el evento como "tpm_min"
        evento = "tpm_min"

        # Se obtienen los datos del evento de la temperatura mínima
        (humedad, uvi, 
         temp_dia, tmp_min, 
         tmp_max, tmp_mañana,
         tmp_tarde, tmp_noche, 
         ssc_term_dia, ssc_term_mañana, 
         ssc_term_tarde, ssc_term_noche) = factor_evento(indice_tpm_min, data, evento)
        
        # Se imprimen los datos del evento de la temperatura mínima
        for x in range(len(fecha_tpm_min)):
            print(f"* En la fecha {fecha_tpm_min[x]} se pronostica" 
                  " una alerta de temperatura mínima")
            print("Los datos del evento son:\n")
            print(f"Humedad relativa: {humedad[x]}%"
                  f" | índice UV: {uvi[x]}")
            print(f"Temperatura promedio durante el día: {temp_dia[x]}°C"
                  f" | Temperatura mínima durante el día: {tmp_min[x]}°C")
            print(f"Temperatura máxima durante el día: {tmp_max[x]}°C"
                  f" | Temperatura promedio durante la mañana: {tmp_mañana[x]}°C")
            print(f"Temperatura promedio durante la tarde: {tmp_tarde[x]}°C"
                  f" | Temperatura promedio durante la noche: {tmp_noche[x]}°C")
            print(f"Sensación térmica promedio durante el día: {ssc_term_dia[x]}°C"
                  f" | Sensación térmica promedio durante la mañana: {ssc_term_mañana[x]}°C")
            print(f"Sensación térmica promedio durante la tarde: {ssc_term_tarde[x]}°C"
                  f" | Sensación térmica promedio durante la noche: {ssc_term_noche[x]}°C\n")

    # Se procesan las alertas de la velocidad del viento
    if "X" in lista_vel_viento:

        # Se obtienen los índices de la lista de velocidad del viento
        indice_vel_viento = indice(lista_vel_viento)

        # Se obtienen las fechas del evento usando los/el índice/s obtenido/s
        fecha_vel_viento = fecha(indice_vel_viento, data)

        # Se formatean las fechas de la velocidad del viento
        for x in range(len(fecha_vel_viento)):
            fecha_vel_viento.append(datetime.fromtimestamp
                                    (fecha_vel_viento[x], timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
            fecha_vel_viento.pop(0)

        # Se establece el evento como "vel_viento"
        evento = "vel_viento"

        # Se obtienen los datos del evento de la velocidad del viento
        (descripcion_evento, presion, 
         nubosidad, vel_viento, 
         dir_viento, rafaga_viento) = factor_evento(indice_vel_viento, data, evento)
        
        # Se imprimen los datos del evento de la velocidad del viento
        for x in range(len(fecha_vel_viento)):
            print(f"* En la fecha {fecha_vel_viento[x]} se pronostica" 
                  " una alerta de velocidad del viento")
            print("Los datos del evento son:\n")
            print(f"Descripción del estado del tiempo: {descripcion_evento[x]}"
                  f" | Presión atmosférica: {presion[x]} hPa")
            print(f"Porcentaje de nubosidad: {nubosidad[x]}%"
                  f" | Velocidad del viento promedio durante el día: {vel_viento[x]} m/s")
            print(f"Dirección del viento: {dir_viento[x]}°"
                  f" | Velocidad máxima de las ráfagas de viento: {rafaga_viento[x]} m/s\n")

    # Se procesan las alertas de la temperatura máxima
    if "X" in lista_tpm_max:

        # Se obtienen los índices de la lista de temperatura mínima
        indice_tpm_max = indice(lista_tpm_max)

        # Se obtienen las fechas del evento usando los/el índice/s obtenido/s
        fecha_tpm_max = fecha(indice_tpm_max, data)

        # Se formatean las fechas de la temperatura máxima
        for x in range(len(fecha_tpm_max)):
            fecha_tpm_max.append(datetime.fromtimestamp
                                 (fecha_tpm_max[x], timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
            fecha_tpm_max.pop(0)

        # Se establece el evento como "tpm_max"
        evento = "tpm_max"

        # Se obtienen los datos del evento de temperatura máxima
        (humedad, uvi, 
         temp_dia, tmp_min, 
         tmp_max, tmp_mañana,
         tmp_tarde, tmp_noche, 
         ssc_term_dia, ssc_term_mañana, 
         ssc_term_tarde, ssc_term_noche) = factor_evento(indice_tpm_max, data, evento)
        
        # Se imprimen los datos del evento de la temperatura máxima
        for x in range(len(fecha_tpm_max)):
            print(f"* En la fecha {fecha_tpm_max[x]} se pronostica" 
                  " una alerta de temperatura máxima")
            print("Los datos del evento son:\n")
            print(f"Humedad relativa: {humedad[x]}%"
                  f" | índice UV: {uvi[x]}")
            print(f"Temperatura promedio durante el día: {temp_dia[x]}°C"
                  f" | Temperatura mínima durante el día: {tmp_min[x]}°C")
            print(f"Temperatura máxima durante el día: {tmp_max[x]}°C"
                  f" | Temperatura promedio durante la mañana: {tmp_mañana[x]}°C")
            print(f"Temperatura promedio durante la tarde: {tmp_tarde[x]}°C"
                  f" | Temperatura promedio durante la noche: {tmp_noche[x]}°C")
            print(f"Sensación térmica promedio durante el día: {ssc_term_dia[x]}°C"
                  f" | Sensación térmica promedio durante la mañana: {ssc_term_mañana[x]}°C")
            print(f"Sensación térmica promedio durante la tarde: {ssc_term_tarde[x]}°C"
                  f" | Sensación térmica promedio durante la noche: {ssc_term_noche[x]}°C\n")
```

## 5. A través de un programa conectese a al menos 3 [API's ](https://apipheny.io/free-api/), obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

```python
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
```