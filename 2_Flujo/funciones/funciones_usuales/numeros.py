# python tiene una libreria especial para funciones matematicas complejas: math
# tenemos que importarla al principio del script
import math

# funciones de conversion

numero = 5
print(float(numero)) # 5.0 racional
print(int(3.3)) # 3 integer (entero)

# redondeo de un numero
numero = 4.567892

print(round(numero, 3)) # matematico

# reto para casa
nota = 4.99999999999
print()

# redondeo a la alta

print(math.ceil(nota))

#redondeo a la baja

print(math.floor(nota))