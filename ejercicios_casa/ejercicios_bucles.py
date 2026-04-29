# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input('dime una palabra: ')

for i in range(10):
    print(palabra)

print('--------')

# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)

edad = int(input('dime tu edad: '))
separador = " "
for i in range(edad):
    print(f'has cumplido' + separador  +  str(i+1) + separador + 'años')


print('------')

# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input('dime un numero: '))

for i in range(1, numero+1, 2):
    print(i, end=", ")


