
num_estudiantes= int(input("ingrese numero de estudiantes: "))

for e in range(num_estudiantes):
    print(f"estudiantes{e + 1}")
    total_notas = 0.0
    for n in range (4):
        nota=float(input(f"ingrese la nota del examen {n + 1}(de 0.0 a 5.0): "))
        total_notas = total_notas + nota

    promedio= total_notas/4

    if promedio >=3.0:
        resultado = "paso"
    else:
        resultado = "perdio"

    print(f"el estudiante {e + 1} {resultado} la materia con un promedio de {promedio:.2f}")

