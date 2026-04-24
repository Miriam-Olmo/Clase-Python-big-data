# metodos de union

nombre = "miriam"
apellido = "olmo"
edad = 33
separador = " - "

texto = f"{nombre}{separador}{apellido}{separador}{edad}"

otro_texto = separador.join([nombre, apellido, str(edad)])
print(texto)
print(otro_texto)


# metodos de separacion

frase = "el presidente dijo: 'como estan los maquinas'"
resultado = frase.partition(": ")
print(resultado)

# split

texto = "porque la vida puede ser maravillosa"
resultado = texto.split(' ')
# para crear un conjunto de elementos sin el espacio en blanco
print(resultado[5])

# splitline() me permite separar lineas en un texto multilinea
cadena = """hola
bienvenido
al
maravilloso
mundo
python
"""
print(cadena)

conjunto_lineas = cadena.splitlines()
print(conjunto_lineas)


# permite deletrear una cadena de texto cualquiera
palabra = "supercalifragilistico"
print(list(palabra))