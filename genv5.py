#Importaciones
from os import remove
import random


#----Variables----
#Variables de entrada
valores_diccionario = int(input("Dime la cantidad de valores quieres que tenga el diccionario: "))
cantidad_frases = int(input("Cuantas frases quieres que genere?: "))
#Datos constantes
caracteres_borrar = '.:/\(),;'
diccionario_palabras = {}
diccionario_frases = {}
#Documentos
documento_sucio = "sentence_list_432.txt"
documento_limpio = "documento_limpio.txt"


#----Funciones----


#Creamos un string para que sea la clave de cada entrada en el diccionario
#Con el formato de "<<palabra>>"
def formato_string_diccionario(array):
    clave = ""
    for item in array:
        clave += "<<"+item+">>"
    return clave


#Creo un documento a partir del documento sucio y quitando los caracteres que no quiero
def limpiar_texto(documento_sucio,documento_limpio,caracteres):
    texto_limpio = open(documento_limpio, "a")
    with open(documento_sucio) as texto:
        for linea in texto:
            linea_limpia = linea.translate(str.maketrans(" "," ",caracteres))
            texto_limpio.write(linea_limpia)
        texto_limpio.close()


#Hago una funcion que cree la frase a partir de un array
def formato_frase(frase_array):
    frase_string = ""
    for palabra in frase_array:
        frase_string += palabra+" "
    frase_string = frase_string.strip()
    return(frase_string)


#Añadimos los valores a los diccionarios aprovechando la funcion de formato
def crear_diccionarios(documento_limpio,diccionario_palabras,diccionario_frases,valores):
    with open(documento_limpio) as documento:
        for frase in documento:
            #Las frases se meten al diccionario como clave y EXIST como valor
            diccionario_frases[frase.rstrip()] = "<<EXIST>>"
            #Parto la frase por las palabras aprovechando las separaciones
            palabras = frase.split()
            #Aqui añado en la frase las palabras en el INICIO y FINAL
            palabras.append("<<FINAL>>")
            for pasada in range(valores):
                palabras.insert(0,"INICIO")
            
            for pos_palabra in range(0,len(palabras)):
                #Doy formato a la clave partiendo el array desde la posicion actual menos el valor a la posicion actual
                clave_array = palabras[pos_palabra-valores:pos_palabra]
                clave_string = formato_string_diccionario(clave_array)
                if clave_string in diccionario_palabras:
                    diccionario_palabras[clave_string].append(palabras[pos_palabra])
                else:
                    diccionario_palabras[clave_string] = [palabras[pos_palabra]]


#La funcion que creara las frases a partir de los diccionarios
def crear_frase_array(diccionario_palabras,valores):
    frase_array = []
    valor = ""
    contador = valores-1
    posicion = 0
    
    for pasada in range(valores-1):
        frase_array.insert(0,"INICIO")
    for pasada in range(valores):
        valor += "<<INICIO>>"
    palabra_creada = random.choice(diccionario_palabras[valor])
    frase_array.append(palabra_creada)
    
    while palabra_creada != "<<FINAL>>":
        valor = formato_string_diccionario(frase_array[posicion:posicion+valores])
        palabra_creada = random.choice(diccionario_palabras[valor])
        frase_array.append(palabra_creada)
        posicion += 1
    del frase_array[0:valores-1]
    del frase_array[len(frase_array)-1]
    return(frase_array)

#----MAIN----
limpiar_texto(documento_sucio,documento_limpio,caracteres_borrar)
crear_diccionarios(documento_limpio,diccionario_palabras,diccionario_frases,valores_diccionario)
print("-----Frases------")
while cantidad_frases != 0:
    frase_array = crear_frase_array(diccionario_palabras,valores_diccionario)
    frase_string = formato_frase(frase_array)
    if frase_string not in diccionario_frases:
        print(frase_string)
        print(" ")
        cantidad_frases -=1
    diccionario_frases[frase_string] = ["<<EXIST>>"]
print("----------------")

remove(documento_limpio)
print(len(diccionario_palabras))