# =============================================================================
# EJERCICIO 1: CALCULADORA CIENTÍFICA ROBUSTA
# Implementa una calculadora que soporte las operaciones:
#   +, -, *, /, // (división entera), % (módulo), ** (potencia), sqrt (raíz cuadrada)
#
# Requisitos de manejo de excepciones:
# - ValueError: si el usuario introduce algo que no es un número
# - ZeroDivisionError: para /, // y %
# - ValueError personalizado: si se pide sqrt de un número negativo
# - ArithmeticError: para desbordamientos en potencias extremas
# - OverflowError: captura específica
# - Excepción genérica como último recurso
# - Bloque finally: siempre muestra "Operación procesada"
# - El programa pide una nueva operación al terminar (recursivo o bucle)

import math 

def pedir_numeros():
        numero1 = float(input('dime un numero: '))
        numero2 = float(input('dime un numero: '))
    

def main():
    menu = """
    ## BIENVENIDO A NUESTRA CALCULADORA CIENTIFICA ROBUSTA ##
    --------------------------------------------------
    [1] Suma
    [2] Resta
    [3] Multiplicacion
    [4] Division
    [5] Division entera
    [6] Modulo
    [7] Potencia
    [8] Raiz cuadrada
    [x] Salir   
    """
    print(menu)
    opcion = input('    ¿Que operación quieres realizar?: ')
    if opcion == '1':
        numeros = pedir_numeros()
        resultado = numeros[0] + numeros[1]
        print(resultado)
    elif opcion == '2':
        numeros = pedir_numeros
        resultado = numeros[0] - numeros[1]
        print(resultado)
    elif opcion == '3':
        numeros = pedir_numeros
        resultado = numeros[0] * numeros[1]
        print(resultado)
    elif opcion == '4':
         numeros = pedir_numeros
         resultado = numeros[0] / numeros[1]
         print(resultado)
    elif opcion == '5':
         numeros = pedir_numeros
         resultado = numeros[0] // numeros[1]
         print(resultado)
    elif opcion == '6':
         numeros = pedir_numeros
         resultado = numeros[0] % numeros[1]
         print(resultado)    
    elif opcion == '7':
         numeros = pedir_numeros
         resultado = numeros[0] ** numeros[1]
         print(resultado)
    elif opcion == '8':
         numeros = pedir_numeros
         resultado = numeros[0] sqrt numeros[1]
    elif opcion == 'x':
        print('vuelve pronto')
        return False
    else:
        print('opcion no valida, introduce de nuevo la opcion. ')
    main()
    
main()