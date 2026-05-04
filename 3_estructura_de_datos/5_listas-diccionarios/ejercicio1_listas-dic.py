# quiero un menu cli, 2 opciones insertar contacto y salir
# crear un lista de contactos vacia.
# contactos = []
# en la opcion 1 inserta contacto pedir los datos de contacto, nombre y telefono. E insertarlo en la lista.
# podremos insertar los contactos que queramos antes de salir
# opcion 2: pintar la lista contactos 

# 	Juan Antonio : 9876543
#   ----------------------
#   Miguel Angel: 567899
#   ----------------------
contactos = []

def insertar_contacto(nombre, tlf, lista):
    #paso 1: crear el diccionario
    contacto_nuevo = {
        'nombre': nombre,
        'telefono': tlf
    }


    # paso 2: añadir el diccionario a la lista
    lista.append(contacto_nuevo)
    print(lista)

def pintar_contactos(lista):
    for contacto in lista:
        print(contacto['nombre'])
        print('_____')
        print(contacto['telefono'])
        print('###')

def main():
    menu = """## Bienvenido a la agenda de contactos ##
[1]. Insertar un contacto
[2]. lista de contactos
[3]. borrar el ultimo contacto de la agenda
[4]. borrar contacto por nombre
[x]. Salir de la app
"""
    print(menu)
    option = input('Dime que opción eliges: ')
    if option == '1':
        nombre = input('Dime el nombre del contacto: ')
        telefono = input('Teléfono de contacto: ')
        insertar_contacto(nombre, telefono, contactos)
    elif option == '2':
        pintar_contactos(contactos)
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    main()



main()
