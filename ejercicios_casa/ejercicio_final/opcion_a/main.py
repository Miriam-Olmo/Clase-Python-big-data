# =====================================================================
    # DEFINICIÓN DE REGLAS DE NEGOCIO PARA CADA FICHERO (Fase 4 y 5)
    # =====================================================================
    
    # --- 1. REGLAS PARA "artistas.csv" ---
    # · nombre: Texto. Si está vacío, marcamos "SIN DATOS".
    # · genero_musical: Texto/Categoría. Mapear según diccionario. Si está vacío, "SIN DATOS".
    # · cache_eur: Entero/Decimal. Si está vacío, marcamos "SIN DATOS". Rango válido: 500 a 500000.
    # · contacto_manager: Texto. Si está vacío, marcamos "SIN DATOS".
    
for i in range(len(artistas)):
    reg = artistas[i]
        
    # Aplicamos normalizar tildes y limpiar espacios
    reg["nombre"] = normalizar_texto(reg.get("nombre"))
    reg["contacto_manager"] = gestionar_vacio_texto(reg.get("contacto_manager"), "SIN DATOS")
    reg["genero_musical"] = limpiar_categoria(reg.get("genero_musical"), generos_dict)
        
    # Tratamiento numérico del caché
    cache_limpio = corregir_numero(reg.get("cache_eur"), valor_por_defecto="SIN DATOS")
    if cache_limpio != "SIN DATOS":
        if cache_limpio < 0: 
            cache_limpio = abs(cache_limpio) # Regla: Precios negativos se pasan a positivo
            
        # Control de rangos lógicos (Fase 8)
        if cache_limpio < 500 or cache_limpio > 500000:
            alertas_manuales.append(f"artistas.csv -> Línea {i+2}: Caché fuera de rango ({cache_limpio}€)")
            reg["cache_eur"] = "REVISAR MANUALMENTE"
        else:
            reg["cache_eur"] = cache_limpio
    else:
        reg["cache_eur"] = "SIN DATOS"


    # --- 2. REGLAS PARA "escenarios_horarios.xlsx" ---
    # · escenario: Texto. Si está vacío, marcamos "SIN DATOS".
    # · artista: Texto. Si está vacío, marcamos "SIN DATOS".
    # · fecha: Texto/Fecha (DD/MM/AAAA). Si está vacío, "FECHA INVÁLIDA".
    # · hora_inicio: Texto. Si está vacío, marcamos "SIN DATOS".
    
for reg in horarios:
    reg["escenario"] = normalizar_texto(reg.get("escenario"))
    reg["artista"] = normalizar_texto(reg.get("artista"))
    reg["fecha"] = limpiar_fecha_manual(reg.get("fecha"))
    reg["hora_inicio"] = gestionar_vacio_texto(reg.get("hora_inicio"), "SIN DATOS")


    # --- 3. REGLAS PARA "ventas_entradas.json" ---
    # · id_venta: Texto/Entero. Identificador único.
    # · comprador: Texto. Si está vacío, marcamos "SIN DATOS".
    # · precio: Decimal. Si está vacío, ponemos 0.0 (valor por defecto). Rango válido: 20 a 500.
    # · fecha_venta: Texto/Fecha (DD/MM/AAAA). Si está vacío, "FECHA INVÁLIDA".
    
for i in range(len(ventas)):
    reg = ventas[i]
    reg["comprador"] = normalizar_texto(reg.get("comprador"))
    reg["fecha_venta"] = limpiar_fecha_manual(reg.get("fecha_venta"))
        
    # Tratamiento del precio: si falta, por defecto decidimos que es 0.0
    precio_limpio = corregir_numero(reg.get("precio"), valor_por_defecto=0.0)
    if precio_limpio < 0: 
        precio_limpio = abs(precio_limpio)
            
    if precio_limpio < 20 or precio_limpio > 500:
        alertas_manuales.append(f"ventas_entradas.json -> Registro {i+1}: Precio fuera de rango ({precio_limpio}€)")
        reg["precio"] = "REVISAR MANUALMENTE"
    else:
        reg["precio"] = precio_limpio


    # --- 4. REGLAS PARA "patrocinadores.xml" ---
    # · nombre_empresa: Texto. Si está vacío, marcamos "SIN DATOS".
    # · importe_patrocinio: Entero/Decimal. Si está vacío, ponemos 0 (valor por defecto). Rango: 1000 a 1000000.
    # · fecha_contrato: Texto/Fecha (DD/MM/AAAA). Si está vacío, "FECHA INVÁLIDA".
    
for i in range(len(patrocinadores)):
    reg = patrocinadores[i]
    reg["nombre_empresa"] = normalizar_texto(reg.get("nombre_empresa"))
    reg["fecha_contrato"] = limpiar_fecha_manual(reg.get("fecha_contrato"))
        
    importe_limpio = corregir_numero(reg.get("importe_patrocinio"), valor_por_defecto=0)
    if importe_limpio < 0: 
        importe_limpio = abs(importe_limpio)
            
    if importe_limpio < 1000 or importe_limpio > 1000000:
        alertas_manuales.append(f"patrocinadores.xml -> Registro {i+1}: Patrocinio fuera de rango ({importe_limpio}€)")
        reg["importe_patrocinio"] = "REVISAR MANUALMENTE"
    else:
        reg["importe_patrocinio"] = importe_limpio