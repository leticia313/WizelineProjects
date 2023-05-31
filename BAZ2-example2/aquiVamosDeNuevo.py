import unittest
def calcular_promedio_notas(estudiantes):
    if not estudiantes:
        return None
    total_estudiantes = len(estudiantes)
    suma_notas = 0
    for estudiante in estudiantes.values():
        suma_notas += estudiante["nota"]
    promedio = suma_notas / total_estudiantes
    return promedio

estudiantes = {
    "Carlos": {"nota": 95},
    "Ivan": {"nota": 80},
    "Luis": {"nota": 58},
    "Jakob": {"nota": 92}
}
print(calcular_promedio_notas(estudiantes))

class TestDiccionario(unittest.TestCase):
    def test_diccionario_datos(self):
       # for nota_est in estudiantes.values():
       #    comparar = nota_est['nota']
      #  aprobo = nota_est = 60
      #  return aprobo
         estudiantes = {
             "Carlos": {"nota": 95},
             "Ivan": {"nota": 80},
             "Luis": {"nota": 58},
             "Jakob": {"nota": 92}
         }

         self.assertEqual(calcular_promedio_notas({"Carlos": {"nota": 95}}), 3)