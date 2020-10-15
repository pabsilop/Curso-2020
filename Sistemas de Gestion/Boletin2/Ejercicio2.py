#Definir una función que calcule la longitud de una lista o una cadena dada.
# (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos
# resulta un muy buen ejercicio.

def longitud_lista(lista):
    for i in lista:
        i +=1
    return i-1
# def longitud_cadena(str1):
#     for i in str1:
#         i +=1
#     return i
#
# str1="Cinco"
# longitudCadena=longitud_cadena(cadena)
# print("La longitud de la cadena es: ",longitudCadena)
lista=[1,2,3,4,5,6,7,8,9]
longitudLista=longitud_lista(lista)
print("La longitud de la lista es: ",longitudLista)


