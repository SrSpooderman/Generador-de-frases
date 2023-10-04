# importar
from os import remove
import random
# variables input
num_cod = int(input("Dime la longitud de codigo que quieres :"))
cant_frases = int(input("Cuantas frases quieres?: "))
# variables datos
del_char = '.:/\(),;'
diccionario = {}
diccionario_frases = {}
documento = "sentence_list_432.txt"
documento_limpio = "documento_limpio.txt"

# formato para diccionario


def dic_key_format(array):
    a = ""
    for item in array:
        a += "<<"+item+">>"
    return a


# limpiar texto
def limpiar_text(documento, documento_limpio):
    texto_limpio = open(documento_limpio, "a")
    with open(documento) as texto:
        for linea in texto:
            linea_limpia = linea.translate(str.maketrans(" ", " ", del_char))
            texto_limpio.write(linea_limpia)
    texto_limpio.close()


# crear diccionarios
def crear_diccionario(documento_limpio, diccionario):
    with open(documento_limpio) as documento:
        for frase in documento:
            diccionario_frases[frase.rstrip()] = "<<EXIST>>"
            palabras = frase.split()
            palabras.append("<<FINAL>>")

            for pasada in range(num_cod):
                palabras.insert(0, "INICIO")

            for pos_palabra in range(0, len(palabras)):
                array_cod = palabras[pos_palabra-num_cod:pos_palabra]
                string_cod = dic_key_format(array_cod)
                if string_cod in diccionario:
                    diccionario[string_cod].append(palabras[pos_palabra])
                else:
                    diccionario[string_cod] = [palabras[pos_palabra]]
    diccionario.pop('')


# crear frases
def crear_frases_nor(num_cod):

    frase_array = []
    for pasada in range(num_cod-1): #reducir a una funcion con un solo for
        frase_array.insert(0, "INICIO")
    valor = ""
    primero = 0
    segundo = num_cod
    for a in range(num_cod):
        valor += "<<INICIO>>"
    palabra_creada = random.choice(diccionario[valor])
    frase_array.append(palabra_creada)
    
    bucle = True
    while bucle: #El condicionante tiene que ser palabra == Final
        valor = dic_key_format(frase_array[primero:segundo])
        palabra_creada = random.choice(diccionario[valor])
        if palabra_creada == "<<FINAL>>":
            bucle = False
        else:
            frase_array.append(palabra_creada)
        primero += 1
        segundo += 1 #segundo es igual a primero + palabras internas
        
    del frase_array[0:num_cod-1] 
    return (frase_array)


# limpiar frase
def limpiar_frase(frase_sucia):
    frase = ""
    for palabra in frase_sucia:
        frase += palabra+" "
    frase_fix = frase.strip()
    return (frase_fix)


# main---
# crear las necesities
limpiar_text(documento, documento_limpio)
crear_diccionario(documento_limpio, diccionario)

# crear la frase o frases
print("-----Frases------")
while cant_frases != 0:
    frase_sucia = crear_frases_nor(num_cod)
    frase_limpia = limpiar_frase(frase_sucia)
    if frase_limpia in diccionario_frases:
        pass
    else:
        print(frase_limpia)
        print(" ")
        cant_frases -= 1
    diccionario_frases[frase_limpia] = ["<<EXIST>>"]
print("----------------")
# limpiar
# print(diccionario)
# print(diccionario_frases)
remove(documento_limpio)
print(len(diccionario))
