

"""dogs = ['sparky','hunter','loki','astro','sparky','rocky','roky','toby','chelsea','maple','maya','loki','sparky','toby','sparky','dexter','fido','sparky']
#crear un diccionario de datos donde cuentes las veces que aparece cada nombre en dogs
dogsvalores = len(dogs)
print(dogsvalores)
#imprime la cantidad de perros que se llaman 'roky' y 'sparky'
repetido=[]
unico=[]
for nombres_repetidos in dogs:
    if nombres_repetidos not in unico:
            unico.append(nombres_repetidos)
    else:
        if nombres_repetidos not in repetido:
            repetido.append(nombres_repetidos)
#Imprime la lista los diferentes nombres de perros
print(unico)


#imprime la cantidad de perros que se llaman 'rocky' y 'sparky'
especifico = repetido(int('rocky','sparky'))
#print(repetido)
print(repetido)

"""


from collections import defaultdict
dogs=['sparky','hunter','loki','astro','sparky','rocky','roky','toby','chelsea','maple','maya','loki','sparky','toby','sparky','dexter','fido','sparky']
dog_dic = defaultdict(int)
for dog in dogs:
    dog_dic[dog] += 1
    print('rocky->',dog_dic['rocky'])
    print('sparky->',dog_dic['sparky'])
    print(list(dog_dic.keys()))
