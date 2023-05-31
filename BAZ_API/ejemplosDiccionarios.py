edades = 0
diccionario = {
    "LEty": {"edad": "35", "clase": "historia"},
    "MArco": {"edad": "30", "clase": "geografia"},
    "Ulises": {"edad": "32", "clase": "geografia"}
}
suma_edades = 0
for clave,value in diccionario.items():
    edad = int(value["edad"])
    suma_edades = edad + suma_edades

print("La suma de edaddes", suma_edades)

print(diccionario.keys())
print(diccionario.values())


