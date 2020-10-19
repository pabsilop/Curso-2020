#Crea un programa en python para rellenar una lista de 15 número enteros:
#Con valores aleatorios entre 1 y 10, y a continuación diga cuantos pares e impares hay.
#Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones que son múltiplos de 3.
#Con los primeros valores de la serie de Fibonacci.
#Con valores introducidos por el usuario, y a continuación que los imprima al revés.
#Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que esté entre 1 o 10.
#Con valores introducidos por el usuario, que deben formar una secuencia creciente.
#Con valores introducidos por el usuario, que no deben estar repetidos.

#Las ejecuciones de las funciones están comentadas
import random

lista = []

#Con valores aleatorios entre 1 y 10, y a continuación diga cuantos pares e impares hay.

def aleatorio_impares():
    impares = 0
    for x in range(15):
        num = random.randrange(10)
        lista.append(num)
        if (num % 2 != 0):
            impares += 1
    print(lista)
    print("Hay ", impares, " numeros impares")

#aleatorio_impares()

#Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones que son múltiplos de 3.
def aleatorio_suma():
    res = 0
    for x in range(15):
        num = random.randrange(10)
        lista.append(num)
    for x in range(len(lista)):
        if (x % 3 == 0):
            res += lista[x]
    print(lista)
    print("La suma de los números en una posición múltiplo de 3 es ", res)

#aleatorio_suma()

#Con los primeros valores de la serie de Fibonacci.



def fibonacci():
    n1=0
    n2=1
    for i in range(15):
        n3=n1+n2
        lista.append(n3)
        n1=n2
        n2=n3
    print(lista)
#fibonacci()

#Con valores introducidos por el usuario, y a continuación que los imprima al revés.
def revertir():
    for x in range(15):
        num = int(input("Introduzca un número: "))
        lista.append(num)
    for i in reversed(lista):
        print(i, end=" ")
#revertir()

#Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que esté entre 1 o 10.

def menor_diez():
    num = 0
    for x in range(15):
        num = int(input("Introduzca un número: "))
        while num < 1 or num > 10:
            print("Número no válido")
            num = int(input("Introduzca un número: "))
        lista.append(num)
    print(lista)
#menor_diez()

#Con valores introducidos por el usuario, que deben formar una secuencia creciente.

def seq_creciente():
    num1 = 0
    num2 = 0
    for x in range(15):
        num2 = num1
        num1 = int(input("Introduzca un número: "))
        while num1 < num2:
            print("Número no válido")
            num1 = int(input("Introduzca un número: "))
        lista.append(num1)
    print(lista)

#seq_creciente()

#Con valores introducidos por el usuario, que no deben estar repetidos.

def lista_no_repetidos():
    num = 0
    for x in range(15):
        num = int(input("Introduzca un número: "))
        while num in lista:
            print("Número no válido")
            num = int(input("Introduzca un número: "))
        lista.append(num)
    print(lista)

#lista_no_repetidos()
