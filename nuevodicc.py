import unittest
def calcular_promedio_notas(estudiantes):
    if not estudiantes:
        return None
    total_estudiantes = len(estudiantes)
    print(total_estudiantes)
#obtener la suma de las notas de los estudiantes
    suma_notas = 0
    for estudiante in estudiantes.values():
            suma_notas += estudiante["nota"]
    promedio = suma_notas / total_estudiantes
    return promedio

estudiantes = {
    "Juan": {"nota": 85},
    "Maria": {"nota": 90},
    "Pedro": {"nota": 78},
    "Ana": {"nota": 92}
}

print(calcular_promedio_notas(estudiantes))


class TestDiccionario(unittest.TestCase):
    def test_diccionario_datos(self):
        estudiantes = {
            "Juan": {"nota": 85},
            "Maria": {"nota": 90},
            "Pedro": {"nota": 78},
            "Ana": {"nota": 92}
        }
        # Prueba 1: Diccionario con notas de estudiantes
        self.assertEqual(calcular_promedio_notas(estudiantes), 86.25)
        #Prueba 2: Diccionario vacio (debe devolver none)
        self.assertIsNone(calcular_promedio_notas({}))
        #Prueba 3: Diccionario con una sola nota
        self.assertEqual(calcular_promedio_notas({"Carlos": {"nota": 80}}), 3)
if __name__ == '__main__':
    unittest.main()
