# quiero saber si una palabra o frase es un palindromo
# Ana => anA
# un palindromo es una palabra que se lee igual al derecho que al reves sin contar mayusculas ni acentos ni espacios en blanco.

# ejemplos de palindromos
#Anita lava la tina.
#Isaac no ronca así.
#Dábale arroz a la zorra el abad.
#Sé verlas al revés.
#Amo la paloma.
# Ojo, Somos, Reconocer


# 1 preguntar por pantalla palabra o frase 
# 2 crear funcion para despues llamarla
# 3 convertir texto en minusculas
# 4 limpiar los espacios
# 5 quitar los acentos
# 6 invertir la frase y comparar
# 7 comprobbar que funciona

palabra_frase = input('introduce la palabra o frase: ')


def es_palindromo(palabra_frase):
    # 1. convertir en minúsculas
    palabra_frase = palabra_frase.lower()
    
    # 2. Quitar espacios
    palabra_frase = palabra_frase.replace(" ", "")
    
    # 3. Quitar acentos
    for inicial, nuevo in [("á","a"), ("é","e"), ("í","i"), ("ó","o"), ("ú","u")]:
        palabra_frase = palabra_frase.replace(inicial, nuevo)
    
    # 4. Invertir y comparar
    if palabra_frase == palabra_frase[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"


resultado = es_palindromo(palabra_frase)
print(f"¿'{palabra_frase}' es palíndromo?: {resultado}")
