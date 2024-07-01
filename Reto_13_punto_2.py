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
