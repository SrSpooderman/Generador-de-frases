import random
char = '.:/\(),'
#Miniprograma de IA, algun tipo de aprendizaje y producir frases. 
#Las fuentes de informacion son unos archivos de texto.
#Las frases de forma estructurar en un diccionario
#Primer paso ver una palabra dentro del texto a partir de esta palabra buscar otras que concuerden con dichas palabras
#De cada palabra ver cual puede ser la siguiente
#Proseguir con la siguiente palabra y la palabra siguiente se metera en la anterior
diccionario = {}
lista = []
frase_nueva = ""
lista_frases = open("sentence_list_432.txt", "r")
#linea = 0
for line in lista_frases:
    #linea +=1
    #print(linea)
    line_clean = line.translate(str.maketrans(" ", " ",char))
    palabras = line_clean.split()
    palabra_anterior= "Incio"
    lista.append(palabras[0])
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
palabra_creada =  (random.choice(lista))
Bucle = True
while Bucle:
    try:
        frase_nueva = frase_nueva + palabra_creada + " " 
        palabra_creada = random.choice(diccionario[palabra_creada])
    except:
        frase_nueva = frase_nueva + "." 
        Bucle = False
print("Frase hecha")
print(frase_nueva)