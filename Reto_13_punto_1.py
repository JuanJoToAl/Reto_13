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
