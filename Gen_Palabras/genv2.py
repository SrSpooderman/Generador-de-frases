"""Que las frases no repitan y no pueden existir"""


#importaciones
import random
#variables
diccionario = {}
palabras_iniciales = [] 
#limpiar linea
def limpiar_linea(linea):
    char = '.:/\(),;'
    linea_limpia = linea.translate(str.maketrans(" "," ",char))
    return(linea_limpia)
#crear diccionario
def crear_diccionario(diccionario, palabras_iniciales):
    with open("sentence_list_432.txt") as documento:
        for linea in documento:
            linea_limpia = limpiar_linea(linea)
            palabras = linea_limpia.split()
            palabra_anterior = "InIcIo"
            palabras_iniciales.append(palabras[0])
            diccionario[palabras[len(palabras)-1]] = ["FiNaL"]
            for palabra in palabras:
                palabra_actual = palabra
                if palabra_anterior in diccionario:
                    try:
                        diccionario[palabra_anterior].append(palabra_actual)
                    except:
                        pass
                else:
                    try:
                        diccionario[palabra_anterior] = [palabra_actual]
                    except:
                        pass
                palabra_anterior = palabra_actual
#crear frase
def crear_frase(palabras_iniciales, diccionario):
    bucle = True
    frase_nueva = ""
    palabra_creada = random.choice(palabras_iniciales)
    while bucle:
        frase_nueva = frase_nueva + palabra_creada + " "
        palabra_creada = random.choice(diccionario[palabra_creada])
        if palabra_creada == "FiNaL":
            frase_nueva = frase_nueva + "."
            bucle = False
    return frase_nueva
#main
crear_diccionario(diccionario, palabras_iniciales)
frase = crear_frase(palabras_iniciales, diccionario)
#Salida
"""print(diccionario)"""
print("Frase creada con exito")
print(frase)