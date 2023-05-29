def calcular_promedio_notas(estudiantes):
    # 1. Definición del diccionario
   """" estudiantes = {
        "Juan": {"nota": 85},
        "Maria": {"nota": 90},
        "Pedro": {"nota": 78},
        "Ana": {"nota": 92}
    }
    """
#total de estudiantes
    total_estudiantes = len(estudiantes)
    print(total_estudiantes)


#obtener la suma de las notas de los estudiantes
suma_notas = 0
for estudiantes in estudiantes.values():
    suma_notas += ["nota"]

    promedio = suma_notas / total_estudiantes
    return promedio

estudiantes = {
        "Juan": {"nota": 85},
        "Maria": {"nota": 90},
        "Pedro": {"nota": 78},
        "Ana": {"nota": 92}
    }
print(calcular_promedio_notas(estudiantes))
