# vamos a ver funciones que me permitan manipular texto.

# funciones que permiten convertir texto sin modificar el original.

texto = "hOLa"

# pasar todo a minusculas

print(texto.lower())

# pasar todo a mayusculas

print(texto.upper())

# texto original
print(texto)

# convertir el texto en capitular
print(title.capitalize())

# convertir la primera letra de cada palabra en mayuscula
print(titulo.title())

# intercambiar mayusculas por minusculas
print(texto.swapcase()) #hOLa => HolA

dni = '456789V'

print( dni.zfill(9) )

# metodos de busqueda dentro de la cadena

frase = 'en un lugar de la mancha'

print(len(frase)) # busca numero de caracteres

# cuantas "a" hay en la cadena
print('numero de as', frase.lower().cont('a'))

# reemplazar un texto por otro
nombre = 'Pablo'
frase = 'David tiene un ferrari'
frase_cambiada = frase.replace('David', nombre)
print(frase)

en esta frase : Como están los maquinas, quitar los espacios

frase = 'Cómo están los maquinas?'


frase_cambiada = frase.replace(" ", "", 2)
print(frase_cambiada)


