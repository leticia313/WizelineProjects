import unittest
class TestDiccionario(unittest.TestCase):
    def test_diccionario_datos(self):
            estudiantes = {
                "Juan": {"nota": 85},
                "Maria": {"nota": 90},
                "Pedro": {"nota": 78},
                "Ana": {"nota": 92}
        }
        estudiantesvalues = estudiantes.values()
        print(estudiantes[0])
        for(int i = 0; i<len(estudiantes); i++)
            print(estudiantesvalues[i])
            estudiante_sum += estudiantesvalues["nota"]


        promedio = estudiantes_sum/len(estudiantes)
