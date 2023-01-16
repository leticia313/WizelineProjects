import numpy as np
import math as mt

def inputTwoVal():
    global Num1, Num2
    Num1 = float(input("Introduce el 1° Valor \n"))
    Num2 = float(input("Introduce el 2° valor \n"))

def inputOneval():
    global NumOne
    NumOne = float(input("Introduce un valor \n"))

def suma(Num1, Num2):
    print(f"La suma de {Num1} + {Num2} = {Num1 + Num2}")

def resta(Num1,Num2):
    print(f"La resta de {Num1} - {Num2} = {Num1 - Num2}")

def multi(Num1,Num2):
    print(f"La multiplicacion de {Num1} * {Num2} = {Num1 * Num2}")

def divi(Num1,Num2):
    if Num2 == 0:
        print("No se puede dividir entre cero")
    else:
        print(f"La division de {Num1} / {Num2}= {Num1 / Num2}")


def raiz(NumOne):
    print(f"La raiz cuadrada de {NumOne} = {np.sqrt(NumOne)}")

def exp(Num1,Num2):
    print(f"El exponente de {Num1} elevado {Num2} = {mt.pow(Num1,Num2)}")

def sen(NumOne):
        print(f"El seno de {NumOne}= {mt.sin(NumOne)}")

def cos(NumOne):
        print(f"El coseno de {NumOne}= {mt.cos(NumOne)}")

def tan(NumOne):
        print(f"La tangente de {NumOne}= {mt.tan(NumOne)}")

def repetOperation(res):
    while True:
        repopc = str(input("Si quieres realizar la misma operación escribe SI, o si lo prefieres regresa al Menú escribiendo NO \n"))
        if repopc == "si":
            operation(res)
        elif repopc == "no":
            break

#All Operation
def operation(opc):
    if opc == 1:
        inputTwoVal()
        suma(Num1,Num2)

    elif opc == 2:
        inputTwoVal()
        resta(Num1,Num2)

    elif opc == 3:
        inputTwoVal()
        multi(Num1,Num2)

    elif opc == 4:
        inputTwoVal()
        divi(Num1,Num2)

    elif opc == 5:
        inputOneval()
        raiz(NumOne)

    elif opc == 6:
        inputTwoVal()
        exp(Num1,Num2)

    elif opc == 7:
        inputOneval()
        sen(NumOne)

    elif opc == 8:
        inputOneval()
        cos(NumOne)

    elif opc == 9:
        inputOneval()
        tan(NumOne)

    elif opc == 10:
        print("Gracias por usar la Calculadora ,¡Vuelve pronto! :D")
        quit()


#Menu operation función principal
def menu():
    while True:
        print("""
        Calculadora
        Indique la operación a realizar
        
        1.Suma
        2.Resta
        3.Multiplicacion        
        4.División
        5.Raiz
        6.Exponente
        7.Seno
        8.Coseno
        9.Tangente
        10.Salir \n""")

        try:
            opc = int(input("Elige una opción de la calculadora: \n"))
        except:
            print("debes escribir un valor, si no seleccionas un valor se cerrara el programa")
            try:
                opc = int(input("Elige una opción de la calculadora: \n"))
            except:
                print("Gracias por usar la Calculadora ,¡Vuelve pronto! :D")
                quit()

        operation(opc)
        repetOperation(opc)

menu()

