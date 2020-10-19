#Definir una función que calcule la longitud de una lista o una cadena dada.
# (Es cierto que python tiene la función len() incorporada, pero escribirla por
# nosotros mismos resulta un muy buen ejercicio.

lista = [1,2,3,4,5,6,7,8,9]
def calcularLongitudLista(lista):
    longitud = 0
    for dia in lista:
        longitud +=1
    return longitud
# print(calcularLongitudLista(lista))
print(f"La longitud de la lista es de {calcularLongitudLista(lista)}")
cadena="Esto es una prueba de cadena"
def calcularLongitudCadena(cadena):
    longitud = 0
    for dia in cadena:
        longitud +=1
    return longitud
print(f"La longitud de la cadena es de {calcularLongitudCadena(cadena)}")
