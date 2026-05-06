from data.trabajadores import trabajadores


def calcular_coste_hora_extra(trabajador):
    # dividimos el sueldo por las horas y sacamos el coste hora
    # multiplicamos por las horas extra y obtenemos el coste_horas_extra
    # se lo añadimos al trabajo clave: valor
    coste_horas_extra = trabajador['sueldo_base'] / trabajador['horas_contrato']
    total_horas_extra = coste_horas_extra * {trabajador['horas_extra']}
    trabajador['total_horas_extra'] = total_horas_extra
    print(trabajador)

for trabajador in trabajadores:
    calcular_coste_hora_extra(trabajador)

#calcular nomina de un trabajador

# calcular nomina de todos los trabajadores

# horas extra sin impuestos