# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input('dime tu nombre: ')
numero = input('dime un numero: ')

print((nombre + "\n") * int(numero))

print('--------')



# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre_completo = input('dime tu nombre completo: ')

print((nombre_completo.lower()), (nombre_completo.upper()), (nombre_completo.title()))

print('----------')



# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")


