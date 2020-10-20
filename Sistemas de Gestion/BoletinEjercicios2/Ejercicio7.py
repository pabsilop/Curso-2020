#Crea un programa en python para rellenar una lista de 15 número enteros:
#Con valores aleatorios entre 1 y 10, y a continuación diga cuantos pares e impares hay.
#Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones que son múltiplos de 3.
#Con los primeros valores de la serie de Fibonacci.
#Con valores introducidos por el usuario, y a continuación que los imprima al revés.
#Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que esté entre 1 o 10.
#Con valores introducidos por el usuario, que deben formar una secuencia creciente.
#Con valores introducidos por el usuario, que no deben estar repetidos.

import random
listaNumeros = []

def numerosAletoriosParEImpar(listaNumeros):
    nPares=0
    nImpares = 0
    for i in range(15):
        num = random.randrange(10)
        listaNumeros.append(num)
        if (num % 2 == 0):
            nPares += 1
        if (num % 2 == 1):
            nImpares += 1
    print(listaNumeros)
    print("Pares: ",nPares)
    print("Impares: ",nImpares)



def randomConSuma():
    restoDivision = 0
    for i in range(15):
        num = random.randrange(10)
        listaNumeros.append(num)
    for i in range(len(listaNumeros)):
        if (i % 3 == 0):
            restoDivision += listaNumeros[i]
    print(listaNumeros)
    print(f"Los números que se encuentran en posicones que son multiplos de 3 suman: {restoDivision}")



def conFibonacci():
    a=0
    b=1
    for i in range(15):
        c=a+b
        listaNumeros.append(c)
        a=b
        b=c
    print(listaNumeros)

def delReves():
    for x in range(15):
        introducir = int(input("Que número quiere introducir: "))
        listaNumeros.append(introducir)
    for i in reversed(listaNumeros):
        print(i)

#Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que esté entre 1 o 10.

def introducirMayor10():
    num = 0
    for i in range(15):
        introducir = int(input("Diga Número: "))
        while introducir < 1 or introducir > 10:
            print("El número introducido tiene que estar entre el número 1 y el 10, intentelo de nuevo")
            introducir = int(input("Diga Número: "))
        listaNumeros.append(introducir)
    print(listaNumeros)

#Con valores introducidos por el usuario, que deben formar una secuencia creciente.

def crecientes():
    a, b = 0, 0
    for i in range(15):
        b = a
        a = int(input("Diga Número: "))
        while a <= b:
            print("El número tiene que ser mayor que el anterior, vuelva a intentarlo")
            a = int(input("Diga Número: "))
        listaNumeros.append(a)
    print(listaNumeros)

def repetidos():
    introducido = 0
    for i in range(15):
        introducido = int(input("Diga número: "))
        while introducido in listaNumeros:
            print("Este número ya se encuentra en la lista, tienes que poner uno que no esté, vuelve a intentarlo")
            introducido = int(input("Diga número: "))
        listaNumeros.append(introducido)
    print(listaNumeros)


