"""Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """



from os import name
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from prettytable import PrettyTable
from time import process_time


assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar el tipo de algoritmo de ordenamiento iterativo")
    print("3- Req. 1. Listar cronológicamente los artistas")
    print("4- Req. 2. Listar cronológicamente las adquisiciones")
    print("5- Req. 3. Clasificar las obras de un artista por técnica")
    print("6- Req. 4. Clasificar las obras por la nacionalidad de sus creadores")
    print("7- Req. 5. Transportar obras de un departamento")
    print("8- Req. 6. Proponer una nueva exposición en el museo")
    print("9- (MAP) N obras mas antiguas por tecnica")
    print("10 - (MAP) Cantidad por nacionalidad")
    print("11- Salir del Menu")


def initCatalog(Tipo_Arreglo):
    return controller.initCatalog(Tipo_Arreglo)


def loadData(catalog):
    controller.loadData(catalog)


catalog = None

def imprimirNacionalidades(lista):
    listaImprimir = primerosYUltimos(lista)


def imprimirArtistasCrono(lista):
    if lt.size(lista)>=6:   
        lista = primerosYUltimos(lista)
    for artista in lt.iterator(lista):
        print()
        print('Nombre: ',artista['DisplayName'])
        print('Año Nacimiento: ',artista['BeginDate'])
        print('Año fallecimiento: ' ,artista['EndDate'])
        print('Nacionalidad: '  ,artista['Nationality'])
        print('Genero : '  ,artista['Gender'])
        print('ArtistBio : '  ,artista['ArtistBio'])
        print('WikiQID : '  ,artista['WikiQID'])
        print('ULAN : '  ,artista['ULAN'])

        

    print()

    # IMPRESION NORMAL
    # print('Nombre ---', 'Año nacimiento ---', 'Año fallecimiento ----', 'Nacionalidad ----', 'Genero')
    # for i in range(1, lt.size(listaImprimir) + 1):
    #     print([lt.getElement(listaImprimir, i).get('DisplayName'), lt.getElement(listaImprimir, i).get('BeginDate'),
    #                lt.getElement(listaImprimir, i).get('EndDate'), lt.getElement(listaImprimir, i).get('Nationality'),
    #                lt.getElement(listaImprimir, i).get('Gender')])

    # IMPRESION CON PRETTY TABLE
    


def imprimirObrasCrono(lista):
    if lt.size(lista)>=6:   
        lista = primerosYUltimos(lista)
    for obra in lt.iterator(lista):
        print()
        print('Titulo: ',obra["Title"])
        print('Artista(s): ',obra['Artist'])
        print('Fecha  Adquisicion: ' ,obra['DateAcquired'])
        print('Medio: '  ,obra['Medium'])
        print('Dimensiones : '  ,obra['Dimensions'])
    
    print()

def imprimir3Nacionalidades(lista):
    if lt.size(lista)>=6:   
        lista = primerosYUltimos(lista)
    for obra in lt.iterator(lista):
        print()
        print('Titulo: ',obra["Title"])
        print('Artista(s): ',obra['Artist'])
        print('Fecha  Adquisicion: ' ,obra['DateAcquired'])
        print('Medio: '  ,obra['Medium'])
        print('Dimensiones : '  ,obra['Dimensions'])
        print('Departamneto : '  ,obra['Department'])
        print('Clasificasion : '  ,obra['Classification'])
        print('URL: '  ,obra['URL'])


    
    print()



    


def imprimirObrasTecnica(lista):
    if lt.size(lista)>=6:   
        lista = primerosYUltimos(lista)
    for obra in lt.iterator(lista):
        print()
        print('Titulo: ',obra["Title"])
        print('Artista(s): ',obra['Artist'])
        print('Fecha  Adquisicion: ' ,obra['DateAcquired'])
        print('Medio: '  ,obra['Medium'])
        print('Dimensiones : '  ,obra['Dimensions'])
        print('Departamneto : '  ,obra['Department'])
        print('Clasificasion : '  ,obra['Classification'])
        print('URL: '  ,obra['URL'])





    

def imprimirObrasTransportar(lista):
    if lt.size(lista)>=5:   
        lista = primeros5Lista(lista)
    for obra in lt.iterator(lista):
        print()
        print('Obra ID: ',obra['ObjectID'])
        print('Titulo: ',obra["Title"])
        print('Artista(s): ',obra['Artist'])
        print('Clasificasion : '  ,obra['Classification'])
        print('Fecha  de la obra: ' ,obra['Date'])
        print('Medio: '  ,obra['Medium'])
        print('Dimensiones : '  ,obra['Dimensions'])
        print('Costo: '  ,obra['Transport'])
        print('URL: '  ,obra['URL'])
    print()
       

    
    
def imprimirObrasMasantiguas(lista):
    if lt.size(lista)>=5:   
        lista = primeros5Lista(lista)
    for obra in lt.iterator(lista):
        print()
        print('Obra ID: ',obra['ObjectID'])
        print('Titulo: ',obra["Title"])
        print('Medio: '  ,obra['Medium'])
        print('Fecha  de la obra: ' ,obra['Date'])
        print('Dimensiones : '  ,obra['Dimensions'])
        print('Artista(s): ',obra['Artist'])
        print('Clasificasion : '  ,obra['Classification'])
        
        
        
        print('Costo: '  ,obra['Transport'])
        print('URL: '  ,obra['URL'])

    print()
       

    
    






    

def imprimirNacionalidades(lista):
    lista=primeros10(lista)
    x = PrettyTable()
    x.field_names = ['Nacionalidad','obras']

    for i in range(1, lt.size(lista) + 1):
        x.add_row([lt.getElement(lista, i).get('name'),lt.size(lt.getElement(lista, i).get('Artworks'))])
    print(x)



def primeros5Lista(lista):
    lista5primeros = lt.newList()
    lt.addLast(lista5primeros, lt.getElement(lista, 1))
    lt.addLast(lista5primeros, lt.getElement(lista, 2))
    lt.addLast(lista5primeros, lt.getElement(lista, 3))
    lt.addLast(lista5primeros, lt.getElement(lista, 4))
    lt.addLast(lista5primeros, lt.getElement(lista, 5))
    return lista5primeros


def ultimos5Lista(lista):
    lista5ultimos = lt.newList()
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista)))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 1))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 2))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 3))
    lt.addLast(lista5ultimos, lt.getElement(lista, lt.size(lista) - 4))
    return lista5ultimos


def primerosYUltimos(lista):
    listaImprimir = lt.newList()
    tam_lista = lt.size(lista)
    lt.addLast(listaImprimir, lt.getElement(lista, 1))
    lt.addLast(listaImprimir, lt.getElement(lista, 2))
    lt.addLast(listaImprimir, lt.getElement(lista, 3))
    lt.addLast(listaImprimir, lt.getElement(lista, tam_lista - 2))
    lt.addLast(listaImprimir, lt.getElement(lista, tam_lista - 1))
    lt.addLast(listaImprimir, lt.getElement(lista, tam_lista))
    return listaImprimir

def primeros10(lista):
    lista10primeros = lt.newList()
    lt.addLast(lista10primeros, lt.getElement(lista, 1))
    lt.addLast(lista10primeros, lt.getElement(lista, 2))
    lt.addLast(lista10primeros, lt.getElement(lista, 3))
    lt.addLast(lista10primeros, lt.getElement(lista, 4))
    lt.addLast(lista10primeros, lt.getElement(lista, 5))
    lt.addLast(lista10primeros, lt.getElement(lista, 6))
    lt.addLast(lista10primeros, lt.getElement(lista, 7))
    lt.addLast(lista10primeros, lt.getElement(lista, 8))
    lt.addLast(lista10primeros, lt.getElement(lista, 9))
    lt.addLast(lista10primeros, lt.getElement(lista, 10))
    return lista10primeros

def resp_req1():
    fecha_inicial = input("Ingresa el año inicial: ")
    fecha_final = input("Ingresa el año final: ")
    Inicio= process_time()
    lista_artistas = controller.listarCronoArtistas(fecha_inicial, fecha_final, catalog)
    tam_lista = lt.size(lista_artistas)
    print("============ Respuesta Requerimiento 1 ============")
    print("La cantidad de artistas nacidos entre " + fecha_inicial + " y " + fecha_final + " es de " + str(tam_lista))
    print("Los primeros 3 y los ultimos 3 artistas en este rango son: ")
    imprimirArtistasCrono(lista_artistas)
    Final=process_time()
    TiempoTotal=Final-Inicio
    print("tarda:"+str(TiempoTotal)+"Mseg")
    


def resp_req2():
    fecha_inicial = input("Ingresa la fecha inicial (AAAA-MM-DD): ")
    fecha_final = input("Ingresa la fecha final (AAAA-MM-DD): ")
    Inicio= process_time()
    lista_obras, cont = controller.listarCronoObras(fecha_inicial, fecha_final, catalog)
    tam_lista = lt.size(lista_obras)
    print("============ Respuesta Requerimiento 2 ============")
    print("Obras adquiridas entre " + fecha_inicial + " y " + fecha_final + " es de " + str(tam_lista))
    #print("La cantidad de obras adquiridas mediante compras es de " + str(cont))
    print("Las primeras 3 y los ultimas 3 obras en este rango son: ")
    imprimirObrasCrono(lista_obras)
    Final=process_time()
    TiempoTotal=Final-Inicio
    print("tarda:"+str(TiempoTotal)+"Mseg")

def resp_req3():
    nombre = input("Ingresa el nombre del artista: ")
    Inicio= process_time()
    tot_obras,tot_tecnica,tecnicaMayor,lista_tecnicamayor,id=controller.tecnica(catalog,nombre)
    print("============ Respuesta Requerimiento 3 ============")
    print("El total de la obras del artista " + nombre + " identificado con el ID" +str(id) +"es de: " + str(tot_obras))
    print("El total de tecnicas utilizadas son de: " + str(tot_tecnica ))
    print("La tecnica mas utilizada es la de: " + tecnicaMayor + " y su cantidad de obras con esta tecnica es de: " + str(
            lt.size(lista_tecnicamayor)))
    imprimirObrasTecnica(lista_tecnicamayor)
    Final=process_time()
    TiempoTotal=Final-Inicio
    print("tarda:"+str(TiempoTotal)+"Mseg")
    
    

def resp_req4():
    Inicio= process_time()
    lista_nacionalidades = controller.nacionalidadyobras(catalog)
    print("El top 10  de nacionalidades en el MOMA es:")
    imprimirNacionalidades(lista_nacionalidades)
    listaUnica=controller.listaUnica(lt.getElement(lista_nacionalidades,1)["Artworks"])
    print("La nacionalidad Top en el museo es ",lt.getElement(lista_nacionalidades,1)["name"],"con una cantidad de: ",lt.size(listaUnica))
    print("Las primeras y ultimas tres obras de la lista de arte son:")
    imprimir3Nacionalidades(listaUnica)
    Final=process_time()
    TiempoTotal=Final-Inicio
    print("tarda:"+str(TiempoTotal)+"Mseg")
    


def resp_req5():
    Inicio= process_time()
    departamento = input("Ingresa el departamento a consultar: ")
    cantidadObras,peso,totalTransporte,listaOrdenada,listaTransporteOrdenada = controller.obrasDepartamento(
        departamento, catalog)
    print("============ Respuesta Requerimiento 5 ============")
    print("Cantidad de obras a transportar: " + str(cantidadObras))
    print("Peso aproximado de las obras (kg): " + str(round(peso, 3)))
    print("Valor aproximado del transportes (USD): " + str(totalTransporte))
    print("----- Obras mas caras de transportar ------")
    imprimirObrasTransportar(ultimos5Lista(listaTransporteOrdenada))
    print("----- Obras mas antiguas ------")
    imprimirObrasMasantiguas(primeros5Lista(listaOrdenada))
    Final=process_time()
    TiempoTotal=Final-Inicio
    print("tarda:"+str(TiempoTotal)+"Mseg")
    
    
    


def resp_reqlab():
    Inicio = process_time()
    n = int(input("ingrese la cantidad de obras a consultar:"))
    tecnica = input("Ingrese el nombre de la tecnica:")
    listalimpia = controller.Obrasmasantiguas(catalog, tecnica)
    Final = process_time()
    print("============ Respuesta Requerimiento Lab ============")
    TiempoTotal = Final-Inicio
    print("tarda:"+str(TiempoTotal)+"Mseg")


    Cont = 0
    for artwork in lt.iterator(listalimpia):
        if Cont < n:
            print(artwork)
            Cont += 1


def resp_reqlab2():
    nacionalidad = input("Ingrese el nombre de la nacionalidad: ")
    Inicio = process_time()
    cantidad = controller.nacionalidad(catalog, nacionalidad)
    Final = process_time()
    print("============ Respuesta Requerimiento Lab 2 ============")
    print("El total de obras con nacionalidad " + nacionalidad + " es  de: " + str(cantidad))
    TiempoTotal = Final-Inicio
    print("tarda:"+str(TiempoTotal)+"Mseg")
    


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs) == 1:
        tipo_Arreglo = ""
        opcion = int(input("Elige la opción 1.ArrayList 2.SingleLinked : "))
        if opcion == 1:
            tipo_Arreglo = "ARRAY_LIST"
        else:
            tipo_Arreglo = "SINGLE_LINKED"
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo_Arreglo)
        Inicio = process_time()
        loadData(catalog)
        Final = process_time()
        TiempoTotal = Final-Inicio
        print("tarda:"+str(TiempoTotal)+"Mseg")


        

        print('Artistas cargados: ' + str(lt.size(catalog['artist'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))

    elif int(inputs) == 2:
        tipo_Algoritmo = input("Elige la opción Insertion, Shell, Merge o Quick Sorts: ")
        ordenado = controller.AlgoritmoIterativo(tipo_Algoritmo, catalog)
        print("Para el catálogo con el tipo de ordenamiento:", tipo_Algoritmo, "el tiempo de procesamiento es:",
              round(ordenado, 2), " milisegundos")

    elif int(inputs) == 3:
        resp_req1()

    elif int(inputs) == 4:
        resp_req2()

    elif int(inputs) == 5:
        resp_req3()

    elif int(inputs) == 6:
        resp_req4()

    elif int(inputs) == 7:
        resp_req5()

    elif int(inputs) == 8:
        A_IO = input("Ingresa el año inicial de las obras: ")
        A_FO = input("Ingresa el año final de las obras: ")
        Area_D = input("Ingresa el área disponible: ")
        print("Propuesta de una nueva exposición:  ")

    elif int(inputs) == 9:
        resp_reqlab()
    elif int(inputs) == 10:
        Inicio = process_time()
        resp_reqlab2()
        Final = process_time()
        print(Final-Inicio)

    else:
        sys.exit(9)