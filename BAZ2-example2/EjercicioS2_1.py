import unittest
def calcular_promedio_notas(estudiantes):
    if not estudiantes:
        return None
    suma_notas = 0
    total_estudiantes = len(estudiantes)
    for estudiante in estudiantes.values():
        suma_notas += estudiante['nota']
    promedio = suma_notas / total_estudiantes
    return promedio

estudiantes = {
    "Carlos": {"nota": 95},
    "Ivan": {"nota": 80},
    "Luis": {"nota": 58},
    "Jakob": {"nota": 92}
}

class TestDiccionario(unittest.TestCase):
    def test(self):
        valid_message = "Aprobado"
        invalid_message = "Reprobado"

    def imprimir_result(invalid_message, valid_message):
        if not [estudiantes.values]:
            return None
        if estudiantes.values('+=50'):
         return invalid_message
        print('Estudiante Aprobado', estudiantes.values())
        if estudiantes.values('+=60'):
            return valid_message
            print('Estudiante reprobado')

if __name__ == '__main__':
    unittest.main()
    print(calcular_promedio_notas(estudiantes))