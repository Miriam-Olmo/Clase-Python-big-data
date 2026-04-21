texto = "Miriam"

#un string es una cadena de caracteres, es decir es un conjunto de caracteres

# cuantos caracteres tiene un texto
print( len(texto) ) #imprime los caracteres que tiene el texto
print(texto[0])  # imprime la M
print(texto[1])  # imprime la i
print(texto[2])  # imprime la r
print(texto[3])  # imprime la i
print(texto[4])  # imprime la a
print(texto[5])  # imprime la m



for i in range(len(texto)):
    print(texto[i])

# upper(pasa a mayuscula) lower(pasa a minuscula)

# coger solo las mayusculas

for i in range(len(texto)):
    if(texto[i] == texto[i].upper()):
        print(texto[i])

#coger solo las minusculas
for i in range(len(texto)):
    if(texto[i] == texto[i].lower()):
        print(texto[i])

