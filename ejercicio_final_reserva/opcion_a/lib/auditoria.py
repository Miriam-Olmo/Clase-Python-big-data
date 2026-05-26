def es_vacio_auditoria(valor):
    """Detecta de forma estricta si un valor está conceptualmente vacío en bruto."""
    if valor is None:
        return True
    cadena = str(valor).strip().lower()
    valores_nulos = ["", "n/a", "-", "no disponible", "vacio", "none", "undefined"]
    return cadena in valores_nulos


def calcular_vacios_por_columna(datos):
    """Cuenta cuántos valores vacíos existen por cada columna/campo."""
    if not datos:
        return {}
    
    # Inicializamos el diccionario de contadores con las columnas del primer registro
    columnas = datos[0].keys()
    contadores = {col: 0 for col in columnas}
    
    for registro in datos:
        for columna in columnas:
            if es_vacio_auditoria(registro.get(columna)):
                contadores[columna] += 1
                
    return contadores


def calcular_duplicados(datos, campos_clave):
    """Calcula cuántos registros repetidos existen según una clave combinada."""
    vistos = set()
    conteo_duplicados = 0
    
    for registro in datos:
        # Creamos una tupla con los valores clave 
        clave = tuple(str(registro.get(campo, "")).strip().lower() for campo in campos_clave)
        
        if clave in vistos:
            conteo_duplicados += 1
        else:
            vistos.add(clave)
            
    return conteo_duplicados


def detectar_valores_anomalos(datos, columna, tipo_validacion):
    """Detecta datos fuera de rango o con incoherencias de formato básicas."""
    conteo_anomalias = 0
    
    for registro in datos:
        valor = registro.get(columna)
        if es_vacio_auditoria(valor):
            continue  # Los vacíos ya los cuenta la otra función, no los duplicamos aquí
            
        cadena = str(valor).strip()
        
        if tipo_validacion == "numerico_negativo":
            # Detecta si un importe es menor o igual a cero
            # Quitamos símbolos comunes de texto temporalmente para evaluar el signo
            prueba = cadena.replace("€", "").replace("$", "").replace(" ", "").replace(",", ".")
            try:
                if float(prueba) <= 0:
                    conteo_anomalias += 1
            except ValueError:
                conteo_anomalias += 1  # Si ni siquiera es un número ejecutable, es una anomalía
                
        elif tipo_validacion == "dni_corrupto":
            # Detecta DNI que no cumplen con tener longitud aproximada o caracteres mixtos
            if len(cadena) <= 8 or len(cadena) >= 10:
                conteo_anomalias += 1
                
    return conteo_anomalias




def auditar_fichero(nombre_fichero, datos, campos_clave, configuracion_anomalias=None):
    """Genera e imprime el informe estadístico de auditoría de calidad en consola."""
    print(f"\n📊 INFORME DE AUDITORÍA: {nombre_fichero.upper()}")
    print("=" * 60)
    print(f"Total registros analizados: {len(datos)}")
    
    if not datos:
        print("❌ Fichero vacío o sin registros para auditar.")
        print("=" * 60)
        return

    # Análisis de vacíos
    print("\n🔍 Valores Ausentes / Vacíos por Columna:")
    vacios = calcular_vacios_por_columna(datos)
    for col, cantidad in vacios.items():
        porcentaje = (cantidad / len(datos)) * 100
        print(f"   • [{col}]: {cantidad} vacíos ({porcentaje:.1f}%)")
        
    # Análisis de duplicados
    print("\n👥 Análisis de Duplicidad:")
    total_duplicados = calcular_duplicados(datos, campos_clave)
    print(f"   • Registros repetidos basados en la clave {campos_clave}: {total_duplicados}")
    
    # Análisis de anomalías personalizadas (Fase 8 preliminar)
    print("\n⚠️ Valores Anómalos o Fuera de Rango:")
    if configuracion_anomalias:
        for col, tipo in configuracion_anomalias.items():
            anomalos = detectar_valores_anomalos(datos, col, tipo)
            print(f"   • En columna [{col}] con regla '{tipo}': {anomalos} alertas detectadas.")
    else:
        print("   • No se configuraron reglas de rango específicas para este fichero.")
        
    print("=" * 60)