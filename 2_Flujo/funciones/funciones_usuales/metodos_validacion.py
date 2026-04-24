valor = input("dime algo bonito: ")

print(valor.isdigit())  # solo digitos
print(valor.isalpha())   # solo letras
print(valor.isalnum())   # letras y numeros
print(valor.isnumeric())  # solo numeros

# sabaer si una cadena de caracteres empieza, termina o incluye un caracter determinado

texto = " en un lugar de la mancha"
print(texto.startswith('e')) # false
print(texto.endswith('a')) # true

# saber si algo esta incluido

busqueda = input('dime que quieres buscar: ')
resultado = busqueda.lower()in texto.lower()
print('incluido'[resultado])