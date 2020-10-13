""""# 1. Imprimir “Hola mundo” por pantalla.
print("Hola Mundo")

# 2. Crear dos variables numéricas, sumarlas y mostrar el resultado
numero1=5
numero2=7
print(numero1+numero2)

# 3. Mostrar el precio final (con IVA) de un producto con un valor de 100, suponiendo que el IVA es el 21%.
precioProducto=100
iva=21
cien=100
descuento=(precioProducto*iva)/cien
precioFinal=precioProducto-descuento
print(precioFinal)

# 4. De dos números, saber cual es el mayor.
numero1=input("Diga el número 1: ")
numero2=input("Diga el número 2: ")
if numero1>numero2:
    print("El número 1 es mayor")
else:
    print("El número 2 es mayor")

# 5. Crea una variable numérica y si está entre 0 y 10, mostrar un mensaje indicándolo.
numero=int(input("Diga un número, si está entre el 0 y el 10 aparecerá un mensaje: "))
if numero >=0 and numero<=10:
    print("El número se encuentra entre el 0 y el 10")

# 6. Añadir al anterior ejercicio, que si está entre 11 y 20, muestre otro mensaje diferente y si está entre 21 y 30 otro mensaje.
numero=int(input("Diga un número: "))
if numero >=0 and numero<=10:
    print("El número se encuentra entre el 0 y el 10")
elif numero>=11 and numero <=20:
    print("El número se encuentra entre el 11 y el 20")
elif numero>=21 and numero <=30:
    print("El número se encuentra entre el 21 y el 30")

# 7. Mostrar con un while los números del 1 al 100.
a=0
while a <100:
    a+=1
    print(a)

# 8. Mostrar con un for los números del 1 al 100.
for i in range(101):
    print(i)

# 9. Implementar un programa en Python que pida un número indeterminado de cadenas de caracteres por el teclado,
# y cuando se finalice dicha introducción, muestre el listado de palabras.
salida=1
lista=[]
while salida != 0:
    cadena=str(input("Diga una palabra: "))
    lista.append(cadena)
    print("Si quiere parar y ver la lista pulse 0 si no pulse cualquier otro número")
    salida=int(input("0 - Parar, Otro número - Otra palabra: "))
print(lista)

# 10. Realiza la misma operación del ejercicio anterior pero con números
salida=1
lista=[]
while salida != 0:
    numero=int(input("Diga un número: "))
    lista.append(numero)
    print("Si quiere parar y ver la lista pulse 0 si no pulse cualquier otro número")
    salida=int(input("0 - Parar, Otro número - Otra número: "))
print(lista)

# 11. Escribe un programa que pida primero un número entero y después pida números enteros hasta
# que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.

# 12. Escribe un programa que genere un número aleatorio entre 0 y 10 y nos pida adivinarlo Tenemos 3 intentos.
import random
numeroRandom=random.randint(0,10)
intentos=0
print("Se ha generado un número aleatorio, entre el 0 y el 10, tiene tres intentos para adivinarlo")
while intentos<=2:
    numeroElegido=int(input("Introduzca el número que cree que es: "))
    if numeroRandom==numeroElegido:
        print("Respuesta correcta")
        intentos=3
    else:
        print("Respuesta incorrecta, pruebe otra vez")
        intentos+=1
print("Felicidades si lo acertaste, si no otra vez será")
"""

# 13. Implementa una función que calcule el factorial de un número. Recuerda que el factorial de un número es el
# producto de todos los números desde ese número hasta 1. Por ejemplo, el factorial de 3, 3!, es 6

# 14. Crea una función en python, triangulo, que reciba un número entero, e imprima un patrón como este por pantalla
tamaño = int(input("Diga el tamaño que quiere que tenga el triángulo: "))

for i in range(1, tamaño + 1):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(1, tamaño):
    for j in range(tamaño - i):
        print("* ", end="")
    print()