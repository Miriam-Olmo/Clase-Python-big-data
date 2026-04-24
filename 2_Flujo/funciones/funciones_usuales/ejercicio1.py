# =============================================================================
# EJERCICIO 1: PROCESADOR DE FRASES
# Pide al usuario una frase.
# Muestra:
#   - La frase con todas las palabras invertidas individualmente
#     (ej: "hola mundo" → "aloh odnum")
#   - devolver la cantidad de caracteres de la frase
#   - El número de veces que aparece cada vocal (a, e, i, o, u)
#   - La frase con los espacios reemplazados por guiones bajos
#   - La frase con palabras invertidad Tony Stark => Stark Tony
# =============================================================================

# primero
frase = "Hola mundo"
lista_caracteres = list(frase)

cantidad2 = len(list(frase))
frase_invertida2 = ""
while(cantidad2 >= 0):
    frase_invertida2 += f'(lista_caracteres[cantidad2-1])'
    cantidad2 -= 1
print(frase_invertida2) 


# segundo
def cantidad_letras(frase):
    contador = 0
    for caracter in frase:
        if caracter.isalpha():
            contador += 1
    return contador
print(cantidad_letras(frase))




frase = "Hola mundo"
nº_caracteres = len(frase)
def contar_vocales(frase,vocal):
    return frase.count(vocal)
    for vocal in 'aeiouáéíóúAEIOUÁÉÍÓÚ':
        print(vocal, contar_vocales(frase,vocal))

def frase_con_separador(frase, separador):
    return frase.replace(" ",separador)

print(frase_con_separador(frase, '_'))

# cuarto

## el avion se estrello por la tormenta
## tormenta la por estrello se avion el

# paso 1 convertir mi frase en una lista
texto = "el avion se estrello por la tormenta"
lista_palabras = texto.split(" ")
cantidad = len(lista_palabras)
frase_invertida = ""


cantidad = len(list(frase))
frase_invertida = ""
while(cantidad >= 0):
    frase_invertida += f'(lista_caracteres[cantidad2-1])'
    cantidad2 -= 1
print(frase_invertida) 
## El avión despegó de la pista
## pista la de despegó avión El

# paso 1: convertir en una lista mi frase
# opcion 1: sin funcion
lista_palabras = texto.split(" ")
cantidad = len(lista_palabras)
frase_invertida = ""
while(cantidad > 0):
    frase_invertida += f"{lista_palabras[cantidad-1]} "
    cantidad -= 1
    
print(frase_invertida)

lista_caracteres = list(texto)
cantidad2 = len(list(texto))
frase_invertida2 = ""
while(cantidad2 > 0):
    frase_invertida2 += f"{lista_caracteres[cantidad2 - 1]}"
    cantidad2 -= 1
    
print( frase_invertida2 )


#opcion 2: con funcion 
def invertir_lista(lista, separador):
    cantidad = len(lista)
    frase_invertida = ""
    while(cantidad > 0):
        frase_invertida += f"{lista[cantidad-1]}" + separador
        cantidad -= 1
    print(frase_invertida)

lista_palabras = texto.split(" ")
invertir_lista(lista_palabras , " ")


lista_caracteres = list(texto)
invertir_lista(lista_caracteres, "")


