# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

edad = int(input('qué edad tienes: '))

if edad < 18:
    print('menor de edad')
else:
    print('mayor de edad')


print('---------')

# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = input('dime tu contraseña: ')
contraseña_guardada = 'Contraseña'
if contraseña_guardada == contraseña.lower():
    print('correxta')
else:
    print('contraseña incorrecta')


