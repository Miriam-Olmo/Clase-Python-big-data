import csv

id = 6

def pedir_datos():
    # para modificar una variable global de una funcion
    global id 
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    correo = input("Correo: ")
    dpto = input('Departamento: ')
    id += 1


def actualizar_datos(carpeta, nombre):
    empleado_nuevo = pedir_datos()
    fichero = open(f"./{carpeta}/{nombre}", 'a', encoding='UTF-8', newline="")
    mi_csv = csv.DictWriter(fichero)
    mi_csv.writerow(empleado_nuevo)

    actualizar_datos('data', 'empleados.csv')