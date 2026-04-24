# replace => se utiliza para limpiar textos

frase = 'Ho)laÇm^u)nd^oÇde)sdeÇp)yth^on'

frase = frase.replace(')', '').replace('^', '').replace('Ç', ' ')
print(frase)

otra_frase = "Él envió más café frío allá después según él también pidió algún té allí recién así él podría reír todavía."
def quitar_acentos(texto):
    return texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
resultado = quitar_acentos(otra_frase)

print(resultado)

otra_frase = otra_frase.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

print(otra_frase)


# eliminar espacios en blanco dentro de una palabra, espacio por delante y por detras de la palabra

nombre = "   Miriam   "
print(f'Hola {nombre.strip()} como estas')
