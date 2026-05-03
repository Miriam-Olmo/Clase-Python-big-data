# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.


materias = ['Matematicas', 'lenguaje', 'historia', 'quimica', 'fisica', 'arte']

print(materias)


# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

for materia in materias:
    print('yo estudio ' + materia)