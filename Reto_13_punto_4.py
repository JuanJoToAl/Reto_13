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
