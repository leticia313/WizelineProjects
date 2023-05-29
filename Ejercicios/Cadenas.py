nombre = 'Leticia Quezada Calzada'
separar = nombre.split()
primero = ''.join(list(reversed(separar[0])))
final = ''.join(list(reversed(separar[2])))
print('Hola mi nombre es {} y me apellido {}'.format(primero,final))



