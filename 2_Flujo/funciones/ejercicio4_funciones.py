



# explicacion previa
# nombre = "Miguel de Unamuno"

# print(nombre[0])

def obtener_iniciales(nombre):
    resultado = ""
    for i in range(len(nombre)):
        if i == 0:
            resultado += nombre[i].upper() + "."
        if nombre[i] == " ":
            resultado += nombre[i+1].upper() + "."
    print(resultado)

obtener_iniciales('azucena fernandez')
