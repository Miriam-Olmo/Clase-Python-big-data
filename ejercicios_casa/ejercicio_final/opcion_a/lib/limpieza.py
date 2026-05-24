def limpiar_texto(texto):
    if texto is None:
        return ""
    texto_str = str(texto)
    
    # primero separa con split y join vuelve a unir
    return " ".join(texto_str.split())


def normalizar_texto(texto):
    correcciones_tildes = {
        "jose":       "José",      "maria":      "María",
        "garcia":     "García",    "gonzalez":   "González",
        "martinez":   "Martínez",  "lopez":      "López",
        "perez":      "Pérez",     "sanchez":    "Sánchez",
        "gomez":      "Gómez",     "fernandez":  "Fernández",
        "rodriguez":  "Rodríguez", "hernandez":  "Hernández",
        "ramirez":    "Ramírez",   "gutierrez":  "Gutiérrez",
    }
    
    # Aplicamos limpiar_texto
    texto_limpio = limpiar_texto(texto)
    if texto_limpio == "":
        return ""
        
    # split() -> corregir palabra a palabra -> join()
    palabras = texto_limpio.split()
    palabras_corregidas = []
    

    for palabra in palabras:
        palabra_minuscula = palabra.lower()
        if palabra_minuscula in correcciones_tildes:
            palabras_corregidas.append(correcciones_tildes[palabra_minuscula])
        else:
            palabras_corregidas.append(palabra.capitalize()) # Formato estándar
            
    return " ".join(palabras_corregidas)



def limpiar_valor_numerico(valor):
    if valor is None:
        return None
        
    # Si ya es un número (int o float), lo devolvemos directamente
    if type(valor) is int or type(valor) is float:
        return valor
        
    valor_texto = str(valor).strip()
    
    # Comprobamos si es un texto que representa un vacío
    if valor_texto in ["", "N/A", "-", "no disponible", "none", "None"]:
        return None
        
    # quitar monedas y limpiar espacios
    valor_texto = valor_texto.replace("€", "").replace("$", "").strip()
    
    if "," in valor_texto and "." in valor_texto:
        valor_texto = valor_texto.replace(".", "")  # Quitamos el punto de miles
        valor_texto = valor_texto.replace(",", ".")  # Cambiamos coma decimal por punto
    elif "," in valor_texto:
 
        partes = valor_texto.split(",")
        if len(partes[-1]) == 3:
            valor_texto = valor_texto.replace(",", "")  # Miles americanos
        else:
            valor_texto = valor_texto.replace(",", ".")  # Decimal europeo
            
    # Intentamos la conversión final con try/except (red de seguridad)
    try:
        if "." in valor_texto:
            return float(valor_texto)
        return int(valor_texto)
    except ValueError:
        return None
    

    def unificar_categoria(valor, diccionario_mapeo, valor_por_defecto="Otros"):
        if valor is None:
            return valor_por_defecto
        
    # Limpiamos los espacios usando la función pequeña que ya teníamos
    valor_limpio = limpiar_texto(valor)
    
    # Si tras limpiar es una cadena vacía o indicador de vacío, salimos
    if valor_limpio in ["", "N/A", "-", "no disponible", "none", "None"]:
        return valor_por_defecto
            
    # Pasamos a minúsculas para que coincida con las claves del diccionario
    valor_minuscula = valor_limpio.lower()
        
    # Buscamos en el mapeo
    if valor_minuscula in diccionario_mapeo:
        return diccionario_mapeo[valor_minuscula]
    else:
        # Si es un género o categoría rara que no estaba en la lista
        return valor_por_defecto