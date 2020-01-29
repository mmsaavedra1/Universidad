from oauth2client import file, client, tools
from googleapiclient import discovery
from MatrizDePagos import *

from pprint import pprint

import httplib2
import webbrowser
import re



# Parametros que se puede cambiar segun el usuario
URl_FORMULARIO = "https://docs.google.com/spreadsheets/d/1b3BbVcRLd43E10QM7nJRmta870fhYdMKy2FRmriVZes/edit#gid=0"
URL_HISTORIAL = "https://docs.google.com/spreadsheets/d/1NrdA_UTaROo8UDsL9jbXqNcI0_gJelmxWM-w02gZICU/edit#gid=0"
URL_BASE_DATOS = "https://docs.google.com/spreadsheets/d/1t8FvCmXm4MOZuCdpGLcDoKhleYzfVBPXpy_NamUaew4/edit#gid=0"


# NO TOCAR
SCOPE = "https://www.googleapis.com/auth/spreadsheets"
FILE_CLIENTE_SECRETO = "client_secret.json"


def obtener_credenciales():
    # Creamos el objeto Flow
    store = file.Storage(FILE_CLIENTE_SECRETO)
    try:
        credenciales = store.get()
    except KeyError:
        flow = client.flow_from_clientsecrets(FILE_CLIENTE_SECRETO, SCOPE)
        credenciales = tools.run_flow(flow, store)

    return credenciales


def obtener_datos(link):
    # Aqui se setean los datos iniciales
    servicio = discovery.build("sheets", "v4", http=HTTP,
                               discoveryServiceUrl=DISCOVERY_URL)

    # Esta es la parte del request
    sheetId = extraer_id(link)

    # Se obtienen los nombres de todas las hojas
    resultado = servicio.spreadsheets().values().get(spreadsheetId=sheetId,
                                                     range="Base de datos").execute()
    respuesta = resultado.get("values", [])
    return respuesta


def extraer_id(link):
    """Metodo para obtener el id de la google sheet"""
    a = re.search("/spreadsheets/d/([a-zA-Z0-9-_]+)", link)
    inicio, final = a.span()
    return link[inicio + 16:final]


def comprobar_hoja(nombre, link):
    """
    :param nombre: Indica el nombre de la hoja que se quiere abrir/crear
    :param link: Indica el link de la hoja que se quiere abrir/crear
    """

    # Se comprueba la existencia de la Sheet, se copia de la original
    # en caso que sea una nueva

    servicio = discovery.build("sheets", "v4", http=HTTP,
                               discoveryServiceUrl=DISCOVERY_URL)
    sheetId = extraer_id(link)

    # 1º Se obtienen el nombre de todas las sheets
    HOJAS = list()
    respuesta = servicio.spreadsheets().get(spreadsheetId=sheetId,
                                            ranges=[],
                                            includeGridData=True).execute()

    # 2º Filtra y almacena el nombre de todas las sheets
    for _respuesta in respuesta["sheets"]:
        HOJAS.append(_respuesta["properties"]["title"])

    # 3º Comprueba si esta la Sheet que deseamos
    #  dentro de la lista de Sheets
    # Se ordenan las sheets de tal forma que queden ordenadas

    if nombre not in HOJAS:
        # Se setea el orden y nombre de la original
        HOJAS.append(nombre)
        HOJAS.sort()
        numero = HOJAS.index(nombre)

        duplicado = {
            "requests": [
                {
                    "duplicateSheet": {
                        "sourceSheetId": 0,
                        "insertSheetIndex": numero,
                        "newSheetName": nombre}
                }
            ]
        }

        servicio.spreadsheets().batchUpdate(body=duplicado,
                                            spreadsheetId=sheetId).execute()


def enviar_datos_formulario(pack):
    """
    Metodo para escribir los datos en la Sheet de formulario
    :param pack: lista con los datos para enviar
    """

    servicio = discovery.build("sheets", "v4", http=HTTP,
                               discoveryServiceUrl=DISCOVERY_URL)

    # Se setean los ID de cada cada GoogleSheet
    formulario_id = extraer_id(URl_FORMULARIO)
    historial_id = extraer_id(URL_HISTORIAL)

    # 1º Desempaquetamos los datos y se organizan
    formulario, historial, nombre_completo, rut, fecha, rbd, actividad = pack
    rut_numeros, rut_digito_verificador = rut.split("-")
    pago = PARAMETROS_2018[PARAMETROS_SIMBOLOGIA_2018[actividad]]

    # Se previenen errores con nombres compuestos
    if len(nombre_completo.split(" ")) >= 4:
        nombre = " ".join(nombre_completo.split(" ")[:-2])
        apellido_paterno = nombre_completo.split(" ")[-2]
        apellido_materno = nombre_completo.split(" ")[-1]
    else:
        nombre, apellido_paterno, apellido_materno = nombre_completo.split(" ")

    # 2º Escribimos los datos en el formulario
    # ****** SIEMPRE SE ESCRIBIRA EN LA FILA 21

    body = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {
                "range": "{}!A21:J21".format(formulario),
                "majorDimension": "ROWS",
                "values": [
                    [rut_numeros, "-", rut_digito_verificador, apellido_paterno,
                     apellido_materno, nombre, " ", " ", "1", pago]
                ]
            }
        ]
    }

    servicio.spreadsheets().values().batchUpdate(spreadsheetId=formulario_id,
                                                 body=body).execute()

    # 3º Agrega una nueva fila ENCIMA de la que se escribio
    body = {
        "requests": [
            {
                "insertDimension": {
                    "range": {
                        "sheetId": str(obtener_sheetId(formulario, URl_FORMULARIO)),
                        "dimension": "ROWS",
                        "startIndex": 20,
                        "endIndex": 21
                    }

                }
            }
        ]
    }

    respuesta = servicio.spreadsheets().batchUpdate(spreadsheetId=formulario_id,
                                                    body=body).execute()

    # 4º Escribimos el historial de actividades
    # ******* SIEMPRE SE ESCRIBIRA EN LA FILA 2
    body = {
        "valueInputOption": "RAW",
        "data": [
            {
                "range": "{}!A2:I2".format(historial),
                "majorDimension": "ROWS",
                "values": [
                    [nombre_completo, nombre, apellido_paterno, apellido_materno,
                     rut, fecha, rbd, actividad, pago]
                ]
            }
        ]
    }

    servicio.spreadsheets().values().batchUpdate(spreadsheetId=historial_id,
                                                 body=body).execute()

    # 5º Agrega una nueva fila ENCIMA de la que se acaba de escribir
    body = {
        "requests": [
            {
                "insertDimension": {
                    "range": {
                        "sheetId": str(
                            obtener_sheetId(historial, URL_HISTORIAL)),
                        "dimension": "ROWS",
                        "startIndex": 1,
                        "endIndex": 2
                    }

                }
            }
        ]
    }

    respuesta = servicio.spreadsheets().batchUpdate(spreadsheetId=historial_id,
                                                    body=body).execute()

    # 6º Se ajusta el formato del texto para cada celda
    body = {
        "requests": [
            {
                "updateSpreadsheetProperties": {
                    "properties":{
                        "defaultFormat":{
                            "horizontalAlignment": "CENTER"
                        }
                    },
                    "fields": "*"
                }
            }
        ]
    }

    respuesta = servicio.spreadsheets().batchUpdate(spreadsheetId=historial_id,
                                                    body=body).execute()

    pprint(respuesta)


def ordenar_informacion(datos):
    """
    Metodo que ordena la informacion de cada fila por columnas almacendada
    en listas
    :param datos: Lista de listas con la informacion de la base de datos
    :return: tupla de listas
    """

    nombre_completo = list()
    rut_completo = list()
    correo_uc = list()

    for persona in datos:
        nombre_completo.append(persona[0])
        rut_completo.append(persona[4])
        correo_uc.append(persona[8])

    return nombre_completo[1:], rut_completo[1:], correo_uc[1:]


def abrir_formulario_google():
    """
    Funcion que abre en explorador la hoja de formulario
    :return:
    """
    webbrowser.open(URl_FORMULARIO)


def abrir_historial_google():
    """
    Funcion que abre en explorador la hoja de historial de actividades
    :return:
    """
    webbrowser.open(URL_HISTORIAL)


def obtener_sheetId(nombre, link):
    """Metodo para obetner el sheetId de la sheet"""

    servicio = discovery.build("sheets", "v4", http=HTTP,
                               discoveryServiceUrl=DISCOVERY_URL)

    sheet_id = extraer_id(link)

    resultado = servicio.spreadsheets().get(spreadsheetId=sheet_id, ranges=[],
                                            includeGridData=True).execute()

    for _respuesta in resultado["sheets"]:
        if _respuesta["properties"]["title"] == nombre:
            return _respuesta["properties"]["sheetId"]


def obtener_spreadsheetId(nombre, link):
    """Metodo para obtener"""


# Parametros que se cargan solo una vez y luego se usan durante el programa
CREDENCIALES = obtener_credenciales()
HTTP = CREDENCIALES.authorize(httplib2.Http())
DISCOVERY_URL = ('https://sheets.googleapis.com/$discovery/rest?'
                 'version=v4')


if __name__ == '__main__':
    # Obtener bas de datos
    obtener_datos("https://docs.google.com/spreadsheets/d/"
                  "1wwFANAAFL-pEdUwm1tniz5cS8yvUnnBaTpBqDFf_CIY/edit#gid=0")

    pprint(obtener_sheetId("Formulario - 1 quincena Marzo", URl_FORMULARIO))
