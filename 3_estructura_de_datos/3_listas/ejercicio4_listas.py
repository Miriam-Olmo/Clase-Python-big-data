# =============================================================================
# EJERCICIO 4: NOTAS DE CLASE — INSERTAR, ORDENAR Y ESTADÍSTICAS
# Tienes una lista de notas de un examen.
# Añade tres notas más con append() y una en la posición 2 con insert().
# Muestra la lista ordenada de mayor a menor.
# Calcula y muestra la media, la nota más alta y la más baja.
# Cuenta cuántos alumnos han aprobado (nota >= 5).
# notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]
# =============================================================================

# menu, pintar el menu con las opciones - lista notas, añadir una nota al final, añadir una nota por posicion, mostrar la lista ordenada, calcular media, calcular maximo, calcular minimo, cuantos alumnos han aprobado. salir

def lista_notas(notas):
    for nota in notas:
        color = "1" if nota < 5 else "2"
        print( f'\033[3{color}m {nota} \033[0m' )
# imprimir en color rojo y verde
# print( f'\033[31m {nota} \033[0m' ) # rojo
# print( f'\033[32m {nota} \033[0m' ) # verde
def nueva_nota(nota,posicion=len(notas)):
    notas.insert(posicion,nota)
    




notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]

def main():
    
    menu = """## Bienvenido a la aplicación de notas ##
    [1]. Listar la notas
    [2]. Añadir nueva nota
    [3]. Añadir nueva nota en cualquier posición
    [4]. Ordenar por mayor a menor
    [5]. Calcular media
    [6]. Calcular máximo
    [7]. Calcular mínimo
    [8]. Numero de alumnos aprobados
    [x]. Salir
    """
    print(menu)
    option = input('Dime que opcion quieres: ')
    print('-' * 40)
    if option == '1':
        lista_notas(notas)
    elif option == '2':
        nota = float((input('que nota quieres añadir: ')))
        nueva_nota(nota)
    elif option == '3':
        nota = float((input('que nota quieres añadir: ')))
        nueva_nota(2,nota)
    elif option == '4':
        print('Ordenar de menor a mayor')
    elif option == '5':
        print('Calcular media')
    elif option == '6':
        print('Calcular maximo')
    elif option == '7':
        print('Calcular minimo')
    elif option == '8':
        print('Cuanto aprobados')
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    print('-' * 40)
    print(' ')
    main()
    


main()