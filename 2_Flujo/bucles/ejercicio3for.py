"""El Asno, el Perro y el Lobo

Caminaban penosamente bajo el Sol, un asno con su carga y el amo seguido del perro.

Llegados a la pradera, el amo cansado se echó a dormir; el burro, entonces, se puso a pacer libremente y solo el perro quedó en peor estado que cuando andaba.

—Compañero, amigo —le dijo al asno— ¿por qué no me haces un espacio para tomar algo de la cesta? El burro respondió, —¿por qué no te esperas un poquito a que despierte el amo y él te sirva la merienda?

De repente, varió la situación por completo, pues un lobo, que acechaba al grupo, se arrojó sobre el cuello del asno.

—¡Socórreme, compañero —gritaba el burro en su agonía—, pero el perro, contemplando la escena desde una altura, repuso: —¿por qué no te esperas un poquito a que despierte el amo y te socorra?
"""


# 1 pedir texto por pantalla

texto = input('dame tu frase: ').lower()
print(texto)

# 2 pedir una vocal

vocal = input('dame una vocal: ').lower()
print(vocal)

# 3 pintar todos los caracteres del texto

cantidad = len(texto)
for i in range(cantidad):
    print(texto[i]) 

# 4 imprimir solo vocal pedida
for i in range(cantidad):
    if texto[i] == vocal:
    print(texto[i])

# 5 contar las vocales. crear una variable que incremente en 1 cada vez que encuentre mi vocal

numero_vocales = 0

for i in range(cantidad):
    if texto[i] == vocal:
        numero_vocales = numero_vocales + 1