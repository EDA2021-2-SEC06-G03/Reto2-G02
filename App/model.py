"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import cmath
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qcks
from DISClib.Algorithms.Sorting import mergesort as mrgs

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos

def newCatalog(Tipo_Arreglo):
    catalog = {'artworks': lt.newList(Tipo_Arreglo),
               'tecnica': None}

    "Indice con tecnica/medio"
    catalog['tecnica'] = mp.newMap(20,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapMedio)
    return catalog


def compareMapMedio(keyname, artwork):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(artwork)
    if keyname == authentry:
        return 0
    elif keyname > authentry:
        return 1
    else:
        return -1


def compareTecnicas(tecnica1, tecnica2):
    if tecnica1 == tecnica2:
        return 0
    elif tecnica1 > tecnica2:
        return 1
    else:
        return 0


# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    art = newArtist(artist['ConstituentID'], artist['DisplayName'],
                    artist['ArtistBio'], artist['Nationality'],
                    artist['Gender'], artist['BeginDate'],
                    artist['EndDate'], artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['artist'], art)


def addArtworks(catalog, artworks):
    artwork = newArtwork(artworks['ObjectID'], artworks['Title'], artworks['ConstituentID'],
                         artworks['Date'], artworks['Medium'], artworks['Dimensions'],
                         artworks['CreditLine'], artworks['AccessionNumber'], artworks['Classification'],
                         artworks['Department'], artworks['DateAcquired'], artworks['Cataloged'],
                         artworks['URL'], artworks['Circumference (cm)'], artworks['Depth (cm)'],
                         artworks['Diameter (cm)'], artworks['Height (cm)'], artworks['Length (cm)'],
                         artworks['Weight (kg)'], artworks['Width (cm)'], artworks['Seat Height (cm)'],
                         artworks['Duration (sec.)'])
    lt.addLast(catalog['artworks'], artwork)
    addTecnica(catalog, artwork)


def addTecnica(catalog, artwork):
    try:
        existeTecnica = mp.contains(catalog['tecnica'], artwork['Medium'])
        if existeTecnica:
            entry = mp.get(catalog['tecnica'], artwork['Medium'])
            tecnica = me.getValue(entry)
        else:
            tecnica = nuevaTecnica(artwork['Medium'])
            mp.put(catalog['tecnica'], artwork['Medium'], tecnica)
        lt.addLast(tecnica['obras'], artwork)
    except Exception:
        return None




def nuevaTecnica(tecnica):
    """
    Esta funcion crea la estructura de obras asociados
    a una tecnica.
    """
    entry = {'tecnica': "", "obra": None}
    entry['tecnica'] = tecnica
    entry['obras'] = lt.newList('SINGLE_LINKED', compareTecnicas)
    return entry


# Funciones para creacion de datos

def newArtist(ConstituentID, DisplayName, ArtistBio, Nationality, Gender, BeginDate, EndDate, WikiQID, ULAN):
    artist = {'ConstituentID': ConstituentID, 'DisplayName': DisplayName, 'ArtistBio': ArtistBio, 'Nacionality': '',
              'Gender': Gender, 'BeginDate': BeginDate, 'EndDate': EndDate, 'WikiQID': WikiQID, 'ULAN': ULAN,
              'Nationality': Nationality}

    return artist


def newArtwork(ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine, AccessionNumber, Classification,
               Department, DateAcquired, Cataloged, URL, Circumference, Depth, Diameter, Height, Length, Weight, Width,
               SeatHeight, Duration):
    artwork = {'ObjectID': ObjectID, 'Title': Title, 'ConstituentID': ConstituentID, 'Date': Date, 'Medium': Medium,
               'Dimensions': Dimensions, 'CreditLine': CreditLine, 'AccessionNumber': AccessionNumber,
               'Classification': Classification, 'Department': Department, 'DateAcquired': DateAcquired,
               'Cataloged': Cataloged, 'URL': URL, 'Circumference': Circumference, 'Depth': Depth,
               'Diameter': Diameter, 'Height': Height, 'Length': Length, 'Weight': Weight, 'Width': Width,
               'SeatHeight': SeatHeight, 'Duration': Duration}

    return artwork


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"] < artwork2["DateAcquired"]:
        r = True
    else:
        r = False
    return r


def cmpArtworkByDate(artwork1, artwork2):
    if artwork1["Date"] < artwork2["Date"]:
        r = True
    else:
        r = False
    return r


def cmpArtworkByTransport(artwork1, artwork2):
    if artwork1["Transport"] < artwork2["Transport"]:
        r = True
    else:
        r = False
    return r


def cmpArtistByBornDate(artist1, artist2):
    if artist1["BeginDate"] < artist2["BeginDate"]:
        r = True
    else:
        r = False
    return r


# Ordenar y clasificar artistas
def cronologicoArtistas(fecha_inicial, fecha_final, catalog):
    start_time = time.process_time()
    lista_ordenada = ins.sort(catalog['artist'], cmpArtistByBornDate)['elements']
    lista_final = lt.newList()
    for artista in lista_ordenada:
        if fecha_final >= artista['BeginDate'] >= fecha_inicial:
            lt.addLast(lista_final, artista)

    stop_time = time.process_time()
    return lista_final, ((stop_time - start_time) * 1000)


def cronologicoObras(fecha_inicial, fecha_final, catalog):
    lista_ordenada = ins.sort(catalog['artworks'], cmpArtworkByDateAcquired)['elements']
    lista_final = lt.newList()
    cont = 0
    for artwork in lista_ordenada:
        if fecha_final >= artwork['DateAcquired'] >= fecha_inicial:
            artwork['Artist'] = ""
            limpio = artwork['ConstituentID'].replace(" ", "").replace("[", "").replace("]", "")
            for artistId in limpio.split(','):
                for artist in catalog['artist']['elements']:
                    if artist['ConstituentID'] == artistId:
                        artwork['Artist'] += artist['DisplayName'] + "\n"
                        break
            lt.addLast(lista_final, artwork)
            if 'Purchase' in artwork['CreditLine'] or 'purchase' in artwork['CreditLine']:
                cont += 1

    return lista_final, cont


# Funciones de artistas y obras
def obtenerIdArtista(nombreArtista, catalog):
    for artist in catalog['artist']['elements']:
        if nombreArtista in artist['DisplayName']:
            return artist['ConstituentID']


def obtenerNombresArtistas(artwork, catalog):
    limpio = artwork['ConstituentID'].replace(" ", "").replace("[", "").replace("]", "")
    nombresArtistas = ""
    for artistId in limpio.split(','):
        for artist in catalog['artist']['elements']:
            if artistId == artist['ConstituentID']:
                nombresArtistas += artist['DisplayName'] + "\n"
    return nombresArtistas


def tecnicaMayorCantidad(listaTecnicas, listaObras):
    tecnicaMayor = ""
    contMayor = 0
    listaObrasMayor = lt.newList()

    # Buscando la tecnica que mas se usó
    for i in range(1, lt.size(listaTecnicas) + 1):
        cont = 0
        for j in range(1, lt.size(listaObras) + 1):
            if lt.getElement(listaTecnicas, i) == lt.getElement(listaObras, j)['Medium']:
                cont += 1
        if cont > contMayor:
            contMayor = cont
            tecnicaMayor = lt.getElement(listaTecnicas, i)

    # Haciendo la lista de las obras con la tecnica mas usada
    for j in range(1, lt.size(listaObras) + 1):
        if lt.getElement(listaObras, j)['Medium'] == tecnicaMayor:
            lt.addLast(listaObrasMayor, lt.getElement(listaObras, j))

    return tecnicaMayor, contMayor, listaObrasMayor


def obtenerValorObra(artwork):
    peso = 0
    m2 = 0
    m3 = 0

    if artwork['Weight'] != "" and artwork['Weight'] != "0":
        peso = float(artwork['Weight'])

    if artwork['Diameter'] != "" and artwork['Diameter'] != "0":
        diametro = float(artwork['Diameter']) / 100
        area = (3.1416 * (diametro / 2) ** 2)
        if artwork['Height'] != "" and artwork['Height'] != "0":
            m3 = (area * (float(artwork['Height']) / 100))
        else:
            m2 = area

    if artwork['Width'] != "" and artwork['Width'] != "0":
        width = float(artwork['Width']) / 100
        if artwork['Length'] != "" and artwork['Length'] != "0":
            area = width * (float(artwork['Length']) / 100)
            if artwork['Depth'] != "" and artwork['Depth'] != "0":
                m3 = area * (float(artwork['Depth']) / 100)
            else:
                m2 = area
        elif artwork['Height'] != "" and artwork['Height'] != "0":
            height = float(artwork['Height']) / 100
            area = width * height
            if artwork['Depth'] != "" and artwork['Depth'] != "0":
                m3 = width * height * (float(artwork['Depth']) / 100)
            else:
                m2 = area
    if peso == 0 and m2 == 0 and m3 == 0:
        valor = 48.00
    elif peso > m2 and peso > m3:
        valor = peso * 72.00
    elif m3 > m2 and m3 > peso:
        valor = m3 * 72.00
    else:
        valor = m2 * 72.00
    return valor


def totalTransporte(lista):
    total = 0
    for i in range(1, lt.size(lista) + 1):
        obra = lt.getElement(lista, i)
        if obra['Transport'] != "" and obra['Transport'] != "0":
            total += float(obra['Transport'])
    return total


def obrasDepartamento(nombreDepartamento, catalog):
    cont = 0
    peso = 0.000
    listaObrasDepartamento = lt.newList()

    for artwork in catalog['artworks']['elements']:
        if nombreDepartamento == artwork['Department']:
            if artwork['Weight'] != "":
                peso += float(artwork['Weight'])
            artwork['Transport'] = round(obtenerValorObra(artwork), 3)
            artwork['Artist'] = obtenerNombresArtistas(artwork, catalog)
            lt.addLast(listaObrasDepartamento, artwork)
            cont += 1
    listaObrasOrdenada = eliminarCampoVacio(ins.sort(listaObrasDepartamento, cmpArtworkByDate), "Date")
    listaTransporteOrdenada = ins.sort(listaObrasDepartamento, cmpArtworkByTransport)
    return cont, listaObrasOrdenada, peso, listaTransporteOrdenada, totalTransporte(listaObrasDepartamento)


def eliminarCampoVacio(lista, nombreCampo):
    listaFiltrada = lt.newList()
    for i in range(1, lt.size(lista) + 1):
        if lt.getElement(lista, i)[nombreCampo] != "":
            lt.addLast(listaFiltrada, lt.getElement(lista, i))
    return listaFiltrada


def totalObras(nombreArtista, catalog):
    idArtista = obtenerIdArtista(nombreArtista, catalog)
    listaTecnicas = lt.newList()
    listaObras = lt.newList()

    for artwork in catalog['artworks']['elements']:
        limpio = artwork['ConstituentID'].replace(" ", "").replace("[", "").replace("]", "")
        for artistId in limpio.split(','):
            if artistId == idArtista:
                tecnicaIncluida = False
                for i in range(1, lt.size(listaTecnicas) + 1):
                    if artwork['Medium'] == lt.getElement(listaTecnicas, i):
                        tecnicaIncluida = True
                        break
                if not tecnicaIncluida:
                    lt.addLast(listaTecnicas, artwork['Medium'])
                lt.addLast(listaObras, artwork)

    # Retorno la cantidad de obras del artista, la cantidad de tenicas diferentes que uso, el id del artista
    # El nombre de la tecnica mas usada, la cantidad de veces que esta se uso y la lista de obras donde se aplico
    tecnicaMayor, contMayor, listaObrasMayor = tecnicaMayorCantidad(listaTecnicas, listaObras)
    return lt.size(listaObras), lt.size(listaTecnicas), idArtista, tecnicaMayor, contMayor, listaObrasMayor


# Funciones de ordenamiento

def AlgoritmoIterativo(Tipo_Algoritmo, catalog):
    elapsed_time_mseg = 0
    if Tipo_Algoritmo == 'Insertion':
        start_time = time.process_time()
        sorted_list = ins.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    elif Tipo_Algoritmo == 'Shell':
        start_time = time.process_time()
        sorted_list = sa.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    elif Tipo_Algoritmo == 'Merge':
        start_time = time.process_time()
        sorted_list = mrgs.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    elif Tipo_Algoritmo == 'Quick Sorts':
        start_time = time.process_time()
        sorted_list = qcks.sort(catalog['artworks'], cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    return elapsed_time_mseg