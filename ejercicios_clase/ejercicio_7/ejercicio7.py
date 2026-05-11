# crear un programa en python que me permita hacer una lista de la compra, 
# Un menu con tres opciones
   # [1].Añadir un producto (nombre, cantidad)
   # [2].Mostrar Lista de la compra
   # [3]. Borrar lista
   # [x]. Salir 
   
# trabajamos con modulos separados. modulo principal y secundario

# el fichero se llamará lista_compra.txt
from lib.functions import añadir_producto, ver_lista

def main():
    menu = """
[1] añadir producto
[2] mostrar lista compra
[3] borrar lista
[x] salir
"""
    print(menu)

    opcion = input('que opcion quieres: ')
    if opcion == '1':
        nombre = input( 'que producto necesitas: ')
        cantidad = input(' cuantos quieres: ')
        añadir_producto(nombre.lower(), cantidad)
    elif opcion == '2':
        ver_lista('lista_compra.txt')
    elif opcion == '3':
        pass
    elif opcion == 'x':
        print('vuelve pronto')
        return

main()

