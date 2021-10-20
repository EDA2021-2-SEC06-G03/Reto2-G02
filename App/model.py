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
from App.controller import nacionalidad, obras, tecnica
from DISClib.DataStructures.singlelinkedlist import lastElement
import config as cf
import time
from DISClib.ADT import orderedmap as om
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
               'tecnica': None,
               'artist': lt.newList(Tipo_Arreglo),
               'idArtistas': None,
               'nacionalidad': None,
               'fechas':None,
               'fechasObras': None }
    
    
    # 1 indice
    "Indice con tecnica/medio"
    catalog['tecnica'] = mp.newMap(20,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapMedio)
    


                                    
    # 2 indice
    "Indice con id"
    catalog['idArtistas'] = mp.newMap(10000,
                                      maptype='CHAINING',
                                      loadfactor=4.0,
                                      comparefunction=compareMapMedio)

    # 3 indice
    catalog['nacionalidad'] = mp.newMap(50,
                                        maptype='PROBING',
                                        loadfactor=0.8,
                                        comparefunction=compareMapMedio)
     # 4 indice
    catalog['fechas'] = mp.newMap(50,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction= compareMapMedio)
    catalog['fechasObras'] = mp.newMap(50,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction= compareMapMedio)
    catalog['IDobras']=mp.newMap(50,
                                        maptype='CHAINING',
                                        loadfactor=4.0,
                                        comparefunction= compareMapMedio)
    

    

    return catalog

            




# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    art = newArtist(artist['ConstituentID'], artist['DisplayName'],
                    artist['ArtistBio'], artist['Nationality'],
                    artist['Gender'], artist['BeginDate'],
                    artist['EndDate'], artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['artist'], art)
    addIdArtist(catalog, art)
    addFecha(catalog,art["BeginDate"],art)
    
    


def addArtworks(catalog, artworks):
    StartTime=time.process_time()
    
    artwork = newArtwork(artworks['ObjectID'], artworks['Title'], artworks['ConstituentID'],
                         artworks['Date'], artworks['Medium'], artworks['Dimensions'],
                         artworks['CreditLine'], artworks['AccessionNumber'], artworks['Classification'],
                         artworks['Department'], artworks['DateAcquired'], artworks['Cataloged'],
                         artworks['URL'], artworks['Circumference (cm)'], artworks['Depth (cm)'],
                         artworks['Diameter (cm)'], artworks['Height (cm)'], artworks['Length (cm)'],
                         artworks['Weight (kg)'], artworks['Width (cm)'], artworks['Seat Height (cm)'],
                         artworks['Duration (sec.)'])
    
    lt.addLast(catalog['artworks'], artwork)
    addIDOBRAS(catalog, artwork)
    addTecnica(catalog, artwork)
    addFechasObras(catalog,artworks['DateAcquired'],artwork)
    
    
    # Se agregan obras por cada nacionalidad de todos los artistas involucrados
    # Se obtiene la lista de ids de los artistas de la obra
    listaIds = artwork['ConstituentID'].replace(" ", "").replace("[", "").replace("]", "")
    artistas=""
    # Se revisa individualmente
    for artistId in listaIds.split(','):
        # Haciendo uso del indice de los artistas se busca al artista por su id
        entry = mp.get(catalog['idArtistas'], artistId)
        artista = me.getValue(entry)
        # Una vez obtenido se agrega a esa nacionalidad esa obra
        addArtworkNacionality(catalog, artista['Nationality'], artwork)
        addIDOBRAS(catalog,artistId,artwork)
        artistas=artistas + artista["DisplayName"] + ", "
    artwork["Artist"]=artistas


    
    
    
    

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


def addIdArtist(catalog, artist):
    artistas = catalog['idArtistas']
    existId = mp.contains(artistas, artist['ConstituentID'])
    if not existId:
        mp.put(artistas, artist['ConstituentID'], artist)
def addIDOBRAS(catalog,id, artwork):
    obras = catalog['IDobras']
    exist= mp.contains(obras, id)
    if exist:
        entry = mp.get(obras, id)
        obra = me.getValue(entry)
    else:
        obra = newIDObras(id)
        mp.put(obras, id, obra)
    lt.addLast(obra['Artworks'], artwork)

def addArtworkNacionality(catalog, nacionalidad, artwork):
    if nacionalidad=="" or nacionalidad=="Nationality unknown" :
        nacionalidad="Unknown"
    nacionalidades = catalog['nacionalidad']
    existnacionality = mp.contains(nacionalidades, nacionalidad)
    if existnacionality:
        entry = mp.get(nacionalidades, nacionalidad)
        entrynacionality = me.getValue(entry)
    else:
        entrynacionality = newNacionality(nacionalidad)
        mp.put(nacionalidades, nacionalidad, entrynacionality)
    lt.addLast(entrynacionality['Artworks'], artwork)



def Cantidadnacionalidad(catalog, nacionalidad):
    nacionalidades = catalog['nacionalidad']
    existnacionality = mp.contains(nacionalidades, nacionalidad)
    if existnacionality:
        entry = mp.get(nacionalidades, nacionalidad)
        entrynacionality = me.getValue(entry)
        totnacionalidad = lt.size(entrynacionality['Artworks'])
        
        return totnacionalidad
    return 0 
def addFecha(catalog,fecha,artist):
    fechas = catalog['fechas']
    existfecha = mp.contains(fechas, fecha)
    if existfecha:
        entry = mp.get(fechas, fecha)
        entryfecha = me.getValue(entry)
    else:
        entryfecha = newFecha(fecha)
        mp.put(fechas, fecha, entryfecha)
    lt.addLast(entryfecha['Artists'], artist)

def addFechasObras(catalog,fecha,artwork):
    fechasobras = catalog['fechasObras']
    existfecha = mp.contains(fechasobras, fecha)
    if existfecha:
        entry = mp.get(fechasobras, fecha)
        entryfechaobra = me.getValue(entry)
    else:
        entryfechaobra = newFechaObras(fecha)
        mp.put(fechasobras, fecha, entryfechaobra)
    lt.addLast(entryfechaobra['Artworks'], artwork)





def newNacionality(name):
    """
    Crea una nueva estructura para modelar las obras  de un artista
    de acuerdo a su Nacionalidad. Se crea una lista para guardar las
    obras de dicho artista.
    """
    nacionalidad = {'name': "",
                    "Artworks": None,
                    }
    nacionalidad['name'] = name
    nacionalidad['Artworks'] = lt.newList('SINGLE_LINKED', compareArtworksNames)
    return nacionalidad


def nuevaTecnica(tecnica):
    """
    Esta funcion crea la estructura de obras asociados
    a una tecnica.
    """
    entry = {'tecnica': "", 'obras': None}
    entry['tecnica'] = tecnica
    entry['obras'] = lt.newList('SINGLE_LINKED', compareTecnicas)
    return entry
def newFecha(date):
   
  
    fecha = {'date': "",
                    "Artists": None,
                    }
    fecha['Date'] = date
    fecha['Artists'] = lt.newList('SINGLE_LINKED',comparefechas )
    return fecha

def newFechaObras(date):
   
  
    fecha = {'date': "",
                    "Artwork": None,
                    }
    fecha['Date'] = date
    fecha['Artworks'] = lt.newList('SINGLE_LINKED',comparefechas )
    return fecha
def newIDObras(id):
    idobras = {'id': "",
    "Artwork": None}
    idobras['id'] = id
    idobras['Artworks'] = lt.newList('SINGLE_LINKED',comparefechas )
    return idobras





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

def comparefechas(fecha1, fecha2):
    """
    Compara dos fechas
    """
    if (fecha1 == fecha2):
        return 0
    elif (fecha1 > fecha2):
        return 1
    else:
        return -1


def compareMapMedio(keyname, artwork):
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

# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtworksNames(artwork1, artwork2):
    """
    Compara dos nombres de dos obras
    """
    if (artwork1["Title"] == artwork2["Title"]):
        return 0
    elif artwork1["Title"] > artwork2["Title"]:
        return 1
    else:
        return -1

def cmpNacionalidades(nacionalidad1,nacionalidad2):
    if lt.size(nacionalidad1["Artworks"]) > lt.size(nacionalidad2["Artworks"]):
        r=True 
    else:
        r = False
    return r
def cmptecnicas(entry1,entry2):
    if lt.size(entry1['obras']) > lt.size(entry2['obras']):
        r=True 
    else:
        r = False
    return r


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
    lista_artistas = lt.newList()
    fechas=catalog["fechas"]
    for fecha in range(int(fecha_inicial),int(fecha_final)+1):
        fecha=str(fecha)
        existfecha = mp.contains(fechas, fecha)
        if existfecha:
            entry=mp.get(fechas,fecha)
            entryfecha=me.getValue(entry)
            for i in range(1, lt.size(entryfecha["Artists"]) + 1):
                lt.addLast(lista_artistas,lt.getElement(entryfecha["Artists"],i))
    
    return lista_artistas


def cronologicoObras(fecha_inicial, fecha_final, catalog):
    lista_artworks = lt.newList()
    lista_fechas=mp.keySet(catalog["fechasObras"])
    cont = 0
    fechasobras=catalog["fechasObras"]
    for fechaOBRAS in lt.iterator(lista_fechas):
        if  fecha_final >= fechaOBRAS >= fecha_inicial:
            entry=mp.get(fechasobras,fechaOBRAS)
            entryfechaobras=me.getValue(entry)
            for artwork in lt.iterator(entryfechaobras["Artworks"]):
                lt.addLast(lista_artworks,artwork)
                if 'Purchase' in artwork['CreditLine'] or 'purchase' in artwork['CreditLine']:
                    cont += 1
    lista_artworks=ins.sort(lista_artworks,cmpArtworkByDateAcquired)

    return lista_artworks,cont


    

    
def CantidadObras(catalog, id):
    ids = catalog['IDobras']
    existid = mp.contains(ids, id)
    if existid:
        entry = mp.get(ids, id)
        entryid = me.getValue(entry)
        totobras= lt.size(entryid['Artworks'])
        return totobras
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

def nacionalidadyobras(catalog):
    listanacionalidades=lt.newList()
    listallaves = mp.keySet(catalog["nacionalidad"])
    for i in range(1, lt.size(listallaves) + 1):
        entry=mp.get(catalog["nacionalidad"],lt.getElement(listallaves,i))
        Nacionalidad=me.getValue(entry)
        lt.addLast(listanacionalidades,Nacionalidad)
    listanacionalidades=ins.sort(listanacionalidades,cmpNacionalidades)

    #listaOrdenada = ins.sort(me.getValue(listaArtistas)[''], cmpArtworkByDate)

def tecnicaMayorCantidad(catalog):
    listaObrasMayor = lt.newList()
    listallaves = mp.keySet(catalog["tecnica"])
    for i in range(1, lt.size(listallaves) + 1):
        entry=mp.get(catalog["tecnica"],lt.getElement(listallaves,i))
        Tecnica=me.getValue(entry)
        lt.addLast(listaObrasMayor,Tecnica)
    listaObrasMayor=ins.sort(listaObrasMayor,cmptecnicas)
    return  listaObrasMayor

def tecnicasPorArtitas(catalog,name ):
    lista_tecnicas=lt.newList()
    lista_tecnicamayor=lt.newList()
    id=obtenerIdArtista(name) 
    entry=mp.get(catalog["IDobras"],id)
    IDobra=me.getValue(entry)
    obrasArtista=IDobra["Artworks"]
    contmayor=0
    tecnicaMayor=""
    for obra in lt.iterator(obrasArtista):
        tecnicaObra=obra["Medium"]
        exist=False
        for tecnica in lt.iterator(lista_tecnicas):
            if tecnicaObra==tecnica:
                exist=True
        if not exist:
            lt.addLast(lista_tecnicas,tecnicaObra)

    for tecnica in lt.iterator(lista_tecnicas):
        cont=0
        for obra in lt.iterator(obrasArtista):
            if tecnica ==obra["Medium"]:
                cont+=1
        if cont>contmayor:
            contmayor=cont
            tecnicaMayor=tecnica
    for obra in lt.iterator(obrasArtista):
        if obra["Medium"]==tecnicaMayor:
            lt.addLast(lista_tecnicamayor,obra)
       
    
    
    tot_obras=lt.size(obrasArtista)
    tot_tecnica=lt.size(lista_tecnicas)
    return tot_obras,tot_tecnica,tecnicaMayor,lista_tecnicamayor








     
    
    

    


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


def Obrasmasantiguas(catalog, tecnica):
    listaObrasTecnica = mp.get(catalog["tecnica"], tecnica)
    listaOrdenada = ins.sort(me.getValue(listaObrasTecnica)['obras'], cmpArtworkByDate)
    listalimpia = eliminarCampoVacio(listaOrdenada, "Date")

    return listalimpia
def listaUnicaObras(listaObrasNacionalidad):
    listaUnica=lt.newList()
    lt.addLast(listaUnica,lt.getElement(listaObrasNacionalidad,0))
    for i in range(1,lt.size(listaObrasNacionalidad)+1):
        existe=False 
        for j in range(i+1,lt.size(listaObrasNacionalidad)+1):
            if lt.getElement(listaObrasNacionalidad,i)["ConstituentID"]== lt.getElement(listaObrasNacionalidad,j)["ConstituentID"]:
                existe=True
        if not existe: 
            lt.addLast(listaUnica,lt.getElement(listaObrasNacionalidad,i))
    return listaUnica
   
            


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