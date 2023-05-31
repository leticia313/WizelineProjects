import unittest
#import math

# Función a implementar: calcular el área de un triangulo
"""
def calcular_area_triangulo()
print ("Calcular el area de un triangulo")
base = input('ingresa la base del triangulo:')
altura = input('Ingresa la altura del triangulo')
area = int (base) * int(altura)/2.0
print('El resultado es ' + str(area))"""
"""
def calcular_area_triangulo (base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("Base y altura deben ser númericos positivos")
    return  base * altura /2
#print(calcular_area_triangulo(5,8))
#Pruebas unitarias
class TestCalcularAreaTriangulo(unittest.TestCase):
    def test_area_triagulo(self):
        #prueba 1: Triangulo con base 4 y altura 5
        self.assertEqual(calcular_area_triangulo(4,5),10)
        #prueba 2 : Triangulo con base 6 y altura 3
        self.assertEqual(calcular_area_triangulo(6,3),10)
        #prueba 3 : Ttriangulo con base x y altura x
        self.assertEqual(calcular_area_triangulo((3,1),20)

"""

"""
def obtener_iniciales(nombre_completo):
    palabras = nombre_completo.split()
    print(palabras)
    iniciales =[palabra[0].upper() for palabra in palabras]
    print(iniciales)
    return "".join(iniciales)
obtener_iniciales(nombre_completo='Leticia Quezada')

#pruebas unitarias
class TestObtenerIniciales(unittest.TestCase):
    def test_obtener_iniciales(self):
        # prueba 1: Prubeba
        self.assertEqual(obtener_iniciales("Leticia Quezada"), "LQ")
        #self.assertEqual(iniciales('L'), 'Q')


"""

# Ejemplo del profe
# def obterner_promedio(numeros):
# if not numeros:
#   return None
# return sum(numeros) / len(numeros)


"""
#Obtener el promedio de una lista de números
def obtener_promedio(numeros):
    promedio = math.fsum(numeros) / len(numeros)
    return promedio

obtener_promedio(numeros= [34,23,1,4,8,9,23])

#pruebas unitarias
class Test_Obtener_promedio(unittest.TestCase):
    def testObtenerPromedio(self):
        # prueba 1: Prubeba
        self.assertEqual(obtener_promedio([3,4,2,11]), 5)
        self.assertEqual(obtener_promedio([3,4,2,11]), 20)
        self.assertEqual(obtener_promedio([34,23,1,4,8,9,23]), 14)
"""


def calcular_promedio_notas(estudiantes):
    # 1. Definición del diccionario
    estudiantes = {
        "Juan": {"nota": 85},
        "Maria": {"nota": 90},
        "Pedro": {"nota": 78},
        "Ana": {"nota": 92}
    }
    #total de estudiantes
    total_estudiantes = len(estudiantes)
    print(total_estudiantes)

    #  conteo = lien(estudiantes)
    # print("El total de estudiante")

  #  for variables in estudiantes():
     #   print(variables)

# for clave in estudiantes.keys():
# print(clave)
