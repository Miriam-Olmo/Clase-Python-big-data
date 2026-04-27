## hacer un programa en python que permita elegir entre 5 opciones
    # 1- pasar un texto a minuscula
    # 2- contar la cantidad de letras de un string
    # 3- invertir el texto => tony stark - stark tony
    # 4- quitar espacios en blanco del texto y acentos
    # 5- salir
# cualquier opcion no descrita vuelve a ejecutar el programa

## """menu"

def main():
    menu = """elige una opcion
    [1] pasar texto a minusculas
    [2] contar la cantidad de letras de un texto
    [3] invertir el texto
    [4] quitar espacios en blanco y acentos
    [5] salir
    """
    print(menu)
    opcion = input('que opcion quieres? ' )
    if opcion == "1":
        texto = input('dime un texto: ').lower()
        print(texto)
    elif opcion == "2":
        texto = input('dime un texto: ')
        print("la cantidad de letras es:" (len[texto]))
    elif opcion == "3":
        texto = input('dime un texto: ')
        lista = texto.split(" ")
        texto_invertido = ""
        for palabra in lista:
            texto_invertido = palabra + " " + texto_invertido
            return texto_invertido
            print(texto_invertido)
    elif opcion == "4":
        texto = input('dime un texto: ')
        textosinacentosniespacios = texto.replace(' ', '') and texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        print(textosinacentosniespacios)
    elif opcion == '5':
        print('nos vemos pronto')
    else:
        print('elige una opcion valida')
        return main()
  
main()



