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
"""
# 8. Mostrar con un for los números del 1 al 100.
for i in range(101):
    print(i)

# Implementar un programa en Python que pida un número indeterminado de cadenas de caracteres por el teclado,
# y cuando se finalice dicha introducción, muestre el listado de palabras.
